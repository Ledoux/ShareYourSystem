#######################
#
#	Building the SYS exe command
#
#######################

PATH=/Users/ledoux/Documents/ShareYourSystem/Pythonlogy/ShareYourSystem
CXX=g++
ARCH=
CFLAGS=
FILE_0=SYS

all: ${FILE_0}.cpp ${FILE_0} /usr/local/bin/${FILE_0} subsystem

/usr/local/bin/${FILE_0} : ${FILE_0}.cpp
	@echo "\n"
	@echo "=====compile and path ${FILE_0}.cpp =================="
	$(CXX) $(ARCH) ${FILE_0}.cpp -o /usr/local/bin/${FILE_0} $(CFLAGS)
	@echo "\n"

subsystem :
	$(MAKE) -C $(PATH)/Standards/Interfacers/Swiger/ all
	$(MAKE) -C $(PATH)/Specials/Lifers/Lifer/ all

clean :
	$(RM) ${FILE_0}.o /usr/local/bin/${FILE_0}
	$(MAKE) -C $(PATH)/Standards/Interfacers/Swiger/ clean
	$(MAKE) -C $(PATH)/Specials/Lifers/Lifer/ clean
