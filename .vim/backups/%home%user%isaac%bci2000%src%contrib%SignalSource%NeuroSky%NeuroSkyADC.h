Vim�UnDo� � <���Z�2AuS�zD���Ȥg��`�0A���                                     P��.    _�                             ����                                                                                                                                                                                                                                                                                                                                                  V        P���     �         5    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        P���     �                //5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        P���     �         5    5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        P���     �                 P////////////////////////////////////////////////////////////////////////////////   9// $Id: NeuroSkyADC.h 2279 2009-02-12 21:40:22Z gmilsap $   #// Author: griffin.milsap@gmail.com   ;// Description: BCI2000 Source Module for NeuroSky devices.   //   // $BEGIN_BCI2000_LICENSE$   //    N// This file is part of BCI2000, a platform for real-time bio-signal research.   K// [ Copyright (C) 2000-2012: BCI2000 team and many external contributors ]   //    O// BCI2000 is free software: you can redistribute it and/or modify it under the   L// terms of the GNU General Public License as published by the Free Software   M// Foundation, either version 3 of the License, or (at your option) any later   // version.   //    A// BCI2000 is distributed in the hope that it will be useful, but   ///                         WITHOUT ANY WARRANTY   H// - without even the implied warranty of MERCHANTABILITY or FITNESS FOR   N// A PARTICULAR PURPOSE.  See the GNU General Public License for more details.   //    O// You should have received a copy of the GNU General Public License along with   =// this program.  If not, see <http://www.gnu.org/licenses/>.   //    // $END_BCI2000_LICENSE$   P////////////////////////////////////////////////////////////////////////////////5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        P���     �                  5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        P���     �                #include "PrecisionTime.h"5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        P���     �                //#include "NeuroSkyThread.h"5�_�      	                      ����                                                                                                                                                                                                                                                                                                                                                  V        P���     �                #include "lib/thinkgear.h"5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                  V        P���     �                #include <vector>5�_�   	              
          ����                                                                                                                                                                                                                                                                                                                                                  V        P���     �               %class NeuroSkyADC : public GenericADC5�_�   
                 	       ����                                                                                                                                                                                                                                                                                                                                                  V        P���     �      
                        NeuroSkyADC();5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                  V        P���     �   	              virtual      ~NeuroSkyADC();5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                  V        P���     �   	              virtual      ~MindWave();5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V   &    P��     �                   std::vector<float> mDataBlock;     int mSamplingTime;     int mConnectionID;5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V   &    P��    �                 �             5�_�                             ����                                                                                                                                                                                                                                                                                                                                                             P��-    �                �             5��