# 🧱 ABSTRACTION 



# Hiding the inner details or COmplxties showing only
# needfull features

from abc import abstractmethod,ABC

class Vehical(ABC):
    @abstractmethod
    def start(self):pass
    @abstractmethod
    def end(self):pass
    @abstractmethod
    def tires(self):pass

class Car(Vehical):
    def price(self):print("High Price")
    def start(self):print("STarted.....")


c=Car()
c.price()










# 🔹 **Problem 6 – Abstract Remote Control**


# 🔹 Problem Statement:
# Create an abstract class `RemoteControl` with methods `turn_on()` and `turn_off()`.
# Derive a class `TVRemote` that implements both methods.

# 🧪 Test Case:
# tv = TVRemote()
# tv.turn_on() ➞ "TV is now ON"
# tv.turn_off() ➞ "TV is now OFF"



# 🔹 **Problem 7 – Shape Abstract Class with Area**


# 🔹 Problem Statement:
# Create an abstract class `Shape` with method `area()`.
# Implement this in two classes: `Circle` and `Rectangle`.

# 🧪 Test Case:
# c = Circle(5)
# c.area() ➞ 78.54
# r = Rectangle(4, 6)
# r.area() ➞ 24




# 🔹 **Problem 8 – Vehicle Interface with Engine Controls**


# 🔹 Problem Statement:
# Define an abstract class `Vehicle` with methods `start_engine()` and `stop()`.
# Implement it in class `Car`.

# 🧪 Test Case:
# car = Car()
# car.start_engine() ➞ "Engine started"
# car.stop() ➞ "Engine stopped"




# 🔹 **Problem 9 – MediaPlayer Interface**


# 🔹 Problem Statement:
# Create an interface class `MediaPlayer` with a method `play()`.
# Implement it in `AudioPlayer` and `VideoPlayer`.

# 🧪 Test Case:
# audio = AudioPlayer()
# audio.play() ➞ "Playing audio"
# video = VideoPlayer()
# video.play() ➞ "Playing video"



# 🔹 Problem Statement:
# Create an interface `PaymentGateway` with method `pay(amount)`.
# Implement it in `PayPal`, `Stripe`, and `RazorPay` classes.

# 🧪 Test Case:
# gateways = [PayPal(), Stripe(), RazorPay()]
# for g in gateways: g.pay(100)

# ✅ Output:
# Paying 100 via PayPal
# Paying 100 via Stripe
# Paying 100 via RazorPay






# 🔹 Problem Statement:
# Define an abstract class `Sensor` with method `read_value()`.
# Create classes `TemperatureSensor` and `HumiditySensor` that return mock values.

# 🧪 Test Case:
# temp = TemperatureSensor()
# hum = HumiditySensor()
# temp.read_value() ➞ "Temperature: 25°C"
# hum.read_value() ➞ "Humidity: 60%"





# 🔹 Problem Statement:
# Create an abstract class `Plugin` with method `execute()`.
# Implement it in classes `PDFExporter` and `CSVExporter`.

# 🧪 Test Case:
# plugins = [PDFExporter(), CSVExporter()]
# for p in plugins: p.execute()

# ✅ Output:
# Exporting as PDF
# Exporting as CSV




# 🔹 Problem Statement:
# Build a framework where developers can create custom widgets
# by extending an abstract class `UIWidget` with method `render()`.

# 🧪 Test Case:
# widgets = [Button("Submit"), TextBox("Username")]
# for w in widgets: w.render()

# ✅ Output:
# Rendering Button: Submit
# Rendering TextBox: Username




# 🔹 Problem Statement:
# Create a modular system using abstract base classes for `Logger`, `DataExporter`, `DataFetcher`.
# Implement CSV and JSON versions of each.

# 🧪 Test Case:
# logger = ConsoleLogger()
# logger.log("Test started")
# fetcher = CSVFetcher()
# exporter = JSONExporter()
# fetcher.fetch_data() ➞ "Fetching data from CSV"
# exporter.export("Data") ➞ "Exporting data as JSON"




# 🔹 Problem Statement:
# Design a multi-layer payment system:
# Interface → Implementation → Integration Layer.
# Abstract base `PaymentMethod`, implemented by `CreditCard` and `UPI`, used by `PaymentProcessor`.

# 🧪 Test Case:
# processor = PaymentProcessor(CreditCard())
# processor.process(200) ➞ "Processing payment of 200 using Credit Card"
# processor.method = UPI()
# processor.process(150) ➞ "Processing payment of 150 using UPI"



