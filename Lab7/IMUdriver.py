from mpu9250 import MPU9250
from machine import I2C, Pin, Timer
from board import SDA, SCL
i2c = I2c(id = 0, scl =Pin(SCL), sda = Pin(SDA), freq = 400000)


MPU9250._chip_id = 115
imu = MPU9250(i2c)
def cb(timer):
	print(imu.accel.xyz)
	print(imu.gyro.xyz)
	print(imu.mag.xyz)
	print(imu.temperature)
	print(imu.accel.z)

tim = Timer(4)

tim.init(period = 200, mode = tim.PERIODIC, callback = cb)