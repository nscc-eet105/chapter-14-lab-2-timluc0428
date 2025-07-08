# Tim Lucas
# Lab 14-2
# 2025-07-08

from dataclasses import dataclass

@dataclass
class Computer:
    __cpu_speed: int
    __ram_size: int
    __drive_size: int

    @property
    def cpu_size(self):
        return self.__cpu_speed
    
    @cpu_size.setter
    def cpu_size(self, value):
        if value >= 0:
            self.__cpu_speed = value
        else:
            raise ValueError("Please enter a non-negative number")
    
    @property
    def ram_size(self):
        return self.__ram_size
    
    @ram_size.setter
    def ram_size(self, value):
        if value >= 0:
            self.__ram_size = value
        else:
            raise ValueError("Please enter a non_negative number")
        
    @property
    def drive_size(self):
        return self.__drive_size
    
    @drive_size.setter
    def drive_size(self, value):
        if value >= 0:
            self.__drive_size = value 
        else:
            raise ValueError("Please enter a non_negative number")
        
    def __str__(self):
        return f"Computer(_Computer__cpu_speed={self.__cpu_speed}, _Computer__ram_size={self.__ram_size}, _Computer__drive_size={self.__drive_size})"
    
def main():
    comp1 = Computer(20, 16, 2000)
    comp2 = Computer(50, 32, 5000)

    print(comp1)
    print(comp2)

if __name__ == "__main__":
    main()