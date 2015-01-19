#include <stdio.h>
#include <iostream>
#include <stdlib.h> 
#include <string>

int main( int argc, char *argv[] )
{
	//Define
	std::string InputStr="";
	std::string OptionStr="";

	//Cout
	std::cout<<"Command length is "<<std::endl;
	std::cout<<argc<<std::endl;
	
	//Check
	if(argc>1)
	{

		//Input
		InputStr=argv[1];
		std::cout<<"InputStr is "<<std::endl;
		std::cout<<InputStr<<std::endl;
		
		//Check
		if(argc>2)
		{
			//Option	
			OptionStr=argv[2];		
			std::cout<<"OptionStr is "<<std::endl;
			std::cout<<OptionStr<<std::endl;	
		}
		
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

			//Check
			if(OptionStr == "local")
			{
				system("shellinaboxd -s /:LOGIN&");
			}

			//call the GUI.ipynb
			system("cd ShareYourGUIstem;ipython notebook GUI.ipynb");
		}
	}
	else
	{
		std::cout<<"You need to specify an input"<<std::endl;
	}

	//return 
	return 0;
}