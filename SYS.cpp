#include <stdio.h>
#include <iostream>
#include <stdlib.h> 
#include <string>

int main( int argc, char *argv[] )
{
	int i;
	std::string InputStr=argv[1];

	//std::cout<<InputStr<<std::endl;
	
	//Check
	if(InputStr == "pythonlogize")
	{
		system("cd Pythonlogy;sudo sh install.sh");
	}

	else if(InputStr == "inform")
	{
		system("python inform.py");
	}

	else if(InputStr == "GUI")
	{
		system("cd ShareYourGUIstem;ipython notebook GUI.ipynb");
	}

	//return 
	return 0;
}