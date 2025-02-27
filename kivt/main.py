from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager, SwapTransition
from kivy.clock import Clock
from kivy.core.window import Window
import obd  # Biblioteca OBD
import atexit  # Para fechar OBD corretamente

# Define o tamanho da tela para 480x320
Window.size = (480, 320)

# Tela de Carregamento Inicial
class LoadingScreen(Screen):
    pass

# Tela Principal com Sensores Importantes
class DashboardScreen(Screen):
    bg_color_rpm = [0, 1, 0, 0.2] 
    bg_color_temp_engine = [0, 0, 0, 0.4]  
    
    def go_to_info(self):
        self.manager.current = 'dashboard_info'
    
    def update_background_color_rpm(self, rpm):
        # Altera a cor de fundo conforme o RPM
        if rpm > 2000:
            self.bg_color_rpm = [1, 0, 0, 0.2]  # Vermelho
        else:
            self.bg_color_rpm = [0, 1, 0, 0.2]   # Verde
    
    def update_background_color_temp_engine(self, temp_engine):
        # Altera a cor de fundo conforme o RPM
        if temp_engine > 100:
            self.bg_color_temp_engine = [1, 0, 0, 0.6]  # Vermelho
        elif temp_engine < 60:
            self.bg_color_temp_engine = [0, 0, 1, 0.3]  # Azul
        else:
            self.bg_color_temp_engine = [0, 0, 0, 0.4]   # padrão

# Tela de Informações Adicionais
class DashboardScreenInfo(Screen):
    def go_to_dashboard(self):
        self.manager.current = 'dashboard'

# Aplicativo Principal
class DashboardApp(App):
    def build(self):
        sm = ScreenManager(transition=SwapTransition())

        # Adiciona as telas ao gerenciador
        sm.add_widget(LoadingScreen(name='loading'))
        sm.add_widget(DashboardScreen(name='dashboard'))
        sm.add_widget(DashboardScreenInfo(name='dashboard_info'))

        # Configura a mudança automática após 5 segundos
        Clock.schedule_once(lambda dt: setattr(sm, 'current', 'dashboard'), 5)

        return sm

    def on_start(self):
        # Inicializa a conexão com OBD
        self.connection = obd.OBD()
        if self.connection.is_connected():
            print("Conectado ao OBD!")
        else:
            print("Falha na conexão com OBD!")

        Clock.schedule_interval(self.update_data, 1)  # Atualiza os dados a cada segundo

    def update_data(self, dt):
        if self.connection.is_connected():
            rpm = self.connection.query(obd.commands.RPM)
            speed = self.connection.query(obd.commands.SPEED)
            temp_engine = self.connection.query(obd.commands.ENGINE_COOLANT_TEMP)
            air_temp = self.connection.query(obd.commands.INTAKE_TEMP)
            throttle_load = self.connection.query(obd.commands.THROTTLE_POS)
            fuel_level = self.connection.query(obd.commands.FUEL_LEVEL)
            temp_oil =self.connection.query(obd.commands.OIL_TEMP)
            fuel_rate = self.connection.query(obd.commands.FUEL_RATE)

            # Atualiza a tela principal (DashboardScreen)
            dashboard = self.root.get_screen('dashboard')
            
            dashboard.ids.rpm_label.text = f"RPM: {rpm.value if rpm.value else 0}"
            dashboard.ids.speed_label.text = f"KM/H: {speed.value if speed.value else 0}"
            dashboard.ids.temp_engine_label.text = f"T. Engine: {temp_engine.value if temp_engine.value else 0} °C"
            dashboard_info.ids.oil_temp_label.text = f"T. Oil: {temp_oil.value if temp_oil.value else 0}°C"

            # Atualiza a tela de informações adicionais (DashboardScreenInfo)
            dashboard_info = self.root.get_screen('dashboard_info')
            
            dashboard_info.ids.throttle_load_label.text = f"Tps: {throttle_load.value if throttle_load.value else 0}%"
            dashboard_info.ids.fuel_label.text = f"Gas: {fuel_level.value if fuel_level.value else 0}%"
            dashboard.ids.air_temp_label.text = f"T. Air: {air_temp.value if air_temp.value else 0} °C"
            dashboard_info.ids.fuel_rate_label.text = f"Fuel Rate: {fuel_rate.value if fuel_rate.value else 0} L/h"
            

    def on_stop(self):
        self.connection.close()
        print("Conexão OBD fechada!")

# Garante que a conexão OBD seja fechada ao sair do app
def close_obd_connection():
    if hasattr(DashboardApp, 'connection') and DashboardApp.connection.is_connected():
        DashboardApp.connection.close()
        print("Conexão OBD fechada!")

atexit.register(close_obd_connection)

DashboardApp().run()
