import dearpygui.dearpygui as dpg
from speeds import hdds, flashs, ssds

dpg.create_context()
dpg.create_viewport(title='Custom Title', width=600, height=600)


def calculate(sender, data, user_data):
    capacity = int(dpg.get_value(user_data[0]))
    price = int(dpg.get_value(user_data[1]))
    caprice = str(price / capacity)
    rw = int(dpg.get_value(user_data[2]))
    hdd = hdds.get_hdd_params(rw)
    ssd = ssds.get_ssd_params(rw)
    flash = flashs.get_flash_params(rw)
    dpg.configure_item(hdd_avr_speed, default_value=hdd)
    dpg.configure_item(ssd_avr_speed, default_value=ssd)
    dpg.configure_item(flash_avr_speed, default_value=flash)
    dpg.configure_item(calculated_value, default_value=caprice)


with dpg.window(label="Input data", width=600, height=200):
    dpg.add_text("Disk capacity")
    capacity = dpg.add_input_text(label="Gb", default_value="500", width=75)
    dpg.add_text("Disk price")
    price = dpg.add_input_text(label="Rub", default_value="2000", width=75)
    dpg.add_text("The amount of data to read/write")
    rw_data = dpg.add_input_text(label="Gb", default_value="70", width=75)
    dpg.add_button(label="Calculate",
                   callback=calculate,
                   user_data=[capacity, price, rw_data],
                   height=30, width=200)


with dpg.window(label="Rub per Gb", width=600, height=75, pos=[0, 200]):
    dpg.add_text("Price per Gb - ")
    dpg.add_same_line()
    calculated_value = dpg.add_input_text(label="Rub per Gb", width=50)


with dpg.window(label="Read/Write speed", width=600, height=200, pos=[0, 275]):
    dpg.add_text("HDD:  ")
    dpg.add_same_line()
    hdd_avr_speed = dpg.add_input_text(label="sec", width=75)
    dpg.add_text("SSD:  ")
    dpg.add_same_line()
    ssd_avr_speed = dpg.add_input_text(label="sec", width=75)
    dpg.add_text("Flash:")
    dpg.add_same_line()
    flash_avr_speed = dpg.add_input_text(label="sec", width=75)


dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
