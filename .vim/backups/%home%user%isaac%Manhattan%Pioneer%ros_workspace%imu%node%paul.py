Vim�UnDo� ƛ�Z}���b$�ǌZ1=��������.ڷ   �                 ;       ;   ;   ;    Q0�h    _�                     $       ����                                                                                                                                                                                                                                                                                                                                                             Q0��     �   #   '   �           self.serialfile.flushInput()5�_�                    %       ����                                                                                                                                                                                                                                                                                                                                                             Q0��     �   $   %              5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                             Q0�     �         �          while(found):    �         �            �         �    5�_�                       
    ����                                                                                                                                                                                                                                                                                                                                                             Q0�    �         �          while(found):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             Q0�'    �         �          found = True5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�	     �   �   �   �        sc.start()5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�     �   �   �   �        5�_�      	              �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�I     �   �   �   �        sc.daemon = True5�_�      
           	   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�k    �   �   �   �              print "CAKEEEEEEEEEEEE"5�_�   	              
   R       ����                                                                                                                                                                                                                                                                                                                                                             Q0��     �   Q   S   �            while(1):5�_�   
                        ����                                                                                                                                                                                                                                                                                                                                                             Q0��    �         �          i=05�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�i     �   �   �   �        mindwave=MindWave()5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�j     �   �   �   �        5�_�                   �        ����                                                                                                                                                                                                                                                                                                                            �           �           V        Q0�u     �   �                mindwave=MindWave()     sc=Serial_Communicator()   H  sc.daemon = True # make sc a daemon so we can terminate it with Ctrl-C     sc.start()   %  mindwave.disconnect() #reset status   9  updateServ = rospy.Publisher('/RosAria/cmd_vel', Twist)     rospy.init_node('talker')          while(1):       mindwave.update()   !    level=mindwave.getAttention()       if(level != ""):         print(level)   %    speed = float(level - 50) / 500.0   9    updateServ.publish(Twist(linear=Vector3(speed, 0,0)))5�_�                    �       ����                                                                                                                                                                                                                                                                                                                            �           �           V        Q0�z     �   �   �              5�_�                    �   ;    ����                                                                                                                                                                                                                                                                                                                            �           �           V        Q0�~     �   �              ;      updateServ.publish(Twist(linear=Vector3(speed, 0,0)))5�_�                    S       ����                                                                                                                                                                                                                                                                                                                            �           �           V        Q0��     �   R   T   �             while(self.kill_received):5�_�                    *       ����                                                                                                                                                                                                                                                                                                                            �           �           V        Q0��     �   )   +   �          while(1):5�_�                    *   
    ����                                                                                                                                                                                                                                                                                                                            �           �           V        Q0�    �   )   +   �          while(self.kill_recieved):5�_�                    �   	    ����                                                                                                                                                                                                                                                                                                                                                             Q0�.     �   �   �   �        except: KeyboardInterrupt:5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�1     �   �   �   �        except KeyboardInterrupt:5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�2     �   �   �   �        except: KeyboardInterrupt:5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�8     �   �   �   �      J    sc.daemon = True # make sc a daemon so we can terminate it with Ctrl-C5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�;    �   �   �   �      J    sc.daemon = True # make sc a daemon so we can terminate it with Ctrl-C5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�G     �   �   �   �            print("quitting...")5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�I    �   �                    sc.kill_recieved=True;5�_�                   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�h    �   �                  sc.kill_recieved=True;5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             Q0�u     �          �      #!/usr/bin/env python5�_�                     �        ����                                                                                                                                                                                                                                                                                                                                                             Q0�     �   �   �   �       5�_�      !               �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�     �   �   �   �        except: KeyboardInterrupt5�_�       "           !   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�   	 �   �   �   �        except KeyboardInterrupt5�_�   !   #           "   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0��     �   �   �   �            if(level != ""):5�_�   "   $           #   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0��   
 �   �   �   �          rospy.init_node('talker')5�_�   #   %           $   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�     �   �   �              level = 0;5�_�   $   &           %   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�      �   �   �   �          while(1):5�_�   %   '           &   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�!     �   �   �   �          rospy.init_node('talker')    �   �   �   �          5�_�   &   (           '   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�*     �   �   �   �              print(level)5�_�   '   )           (   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�2     �   �   �   �            if(level != ""):5�_�   (   *           )   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�@    �   �   �   �          rospy.init_node('talker')5�_�   )   +           *   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0��     �   �   �   �      -    old_level = 0 #we force out the inital 0s5�_�   *   ,           +   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0��    �   �   �   �              old_level = level5�_�   +   -           ,   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0��     �   �   �   �      #POOR SIGNAL5�_�   ,   .           -   �   "    ����                                                                                                                                                                                                                                                                                                                                                             Q0�     �   �   �   �      "        signal=str(payload.pop(0))5�_�   -   /           .   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�     �   �   �   �      3        print("Poor Signal=" + str(payload.pop(0)))5�_�   .   0           /   �   %    ����                                                                                                                                                                                                                                                                                                                                                             Q0�     �   �   �   �      5          print("Poor Signal=" + str(payload.pop(0)))5�_�   /   1           0   �   !    ����                                                                                                                                                                                                                                                                                                                                                             Q0�      �   �   �   �      ,          print("Poor Signal=" + str(signal)5�_�   0   2           1   �   )    ����                                                                                                                                                                                                                                                                                                                                                             Q0�"     �   �   �   �      )          print("Poor Signal=" + (signal)5�_�   1   3           2   �   !    ����                                                                                                                                                                                                                                                                                                                                                             Q0�$    �   �   �   �      (          print("Poor Signal=" + (signal5�_�   2   4           3   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�>     �   �   �   �      '          print("Poor Signal=" + signal    �   �   �   �             5�_�   3   5           4   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�H     �   �   �   �      "        signal=str(payload.pop(0))5�_�   4   6           5   �        ����                                                                                                                                                                                                                                                                                                                                                             Q0�I     �   �   �   �      #        signal=str(payload.pop(#0))5�_�   5   7           6   �   '    ����                                                                                                                                                                                                                                                                                                                                                             Q0�T    �   �   �   �      '          print("Poor Signal=" + signal5�_�   6   8           7   �   	    ����                                                                                                                                                                                                                                                                                                                                                             Q0�     �   �   �   �              #old_level = level5�_�   7   9           8   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�     �   �   �   �              old_level = level5�_�   8   :           9   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�J     �   �   �   �      -    old_level = 0 #we force out the inital 0s5�_�   9   ;           :   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�K    �   �   �   �      .    old_level = 0" #we force out the inital 0s5�_�   :               ;   �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�g    �   �   �          '        print "we read Attention value"5�_�                    �       ����                                                                                                                                                                                                                                                                                                                                                             Q0�W     �   �   �              sciiii.kill_recieved=True;5�_�                    �        ����                                                                                                                                                                                                                                                                                                                            �          �          V       Q0�r     �   �   �          mindwave=MindWave()   sc=Serial_Communicator()   Fsc.daemon = True # make sc a daemon so we can terminate it with Ctrl-C   
sc.start()   #mindwave.disconnect() #reset status   7updateServ = rospy.Publisher('/RosAria/cmd_vel', Twist)   rospy.init_node('talker')       	while(1):     mindwave.update()     level=mindwave.getAttention()     if(level != ""):       print(level)   #  speed = float(level - 50) / 500.0   7  updateServ.publish(Twist(linear=Vector3(speed, 0,0)))5��