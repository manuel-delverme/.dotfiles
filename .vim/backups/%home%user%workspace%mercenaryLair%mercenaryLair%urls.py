Vim�UnDo� �8ǲ�`-p��@��'��;���˹ڻq�d;e                    A       A   A   A    R�    _�                            ����                                                                                                                                                                                                                                                                                                                                                             R�t     �               0    # url(r'^admin/', include(admin.site.urls)),5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             R�u     �               /     url(r'^admin/', include(admin.site.urls)),5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             R�x     �               "# from django.contrib import admin5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             R�y     �               ! from django.contrib import admin5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             R�z     �               # admin.autodiscover()5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             R�z    �                admin.autodiscover()5�_�      	                     ����                                                                                                                                                                                                                                                                                                                                                             R��     �                 )5�_�      
           	           ����                                                                                                                                                                                                                                                                                                                                                             R��     �                5�_�   	              
           ����                                                                                                                                                                                                                                                                                                                                                             R��     �                )�                D                          url(r'^admin/', include(admin.site.urls)),�                Q                      url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),�                S                  url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),�                F              url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),�                0          url(r'^polls/$', 'polls.views.index'),5�_�   
                         ����                                                                                                                                                                                                                                                                                                                                                             R��     �                    urlpatterns = patterns('',5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       R��     �               ,      url(r'^polls/$', 'polls.views.index'),   >      url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),   G      url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),   A      url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),5�_�                          ����                                                                                                                                                                                                                                                                                                                                                V       R��     �                0      url(r'^admin/', include(admin.site.urls)),5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       R�     �                      )5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       R�    �                 5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             R�     �               *    url(r'^polls/$', 'polls.views.index'),5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             R�     �                5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             R�     �                                 )g5�_�                           ����                                                                                                                                                                                                                                                                                                                                                       R�     �                                  )�                M                  url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),�                O              url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),�                B          url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),�                urlpatterns = patterns('',5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        R�     �                *    url(r'^polls/$', 'polls.views.index'),   <    url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),   E    url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),   ?    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),       )5�_�                           ����                                                                                                                                                                                                                                                                                                                                                  V        R�     �                    urlpatterns = patterns('',5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        R�    �                      )�                A      url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),�                G      url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),�                >      url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),�                ,      url(r'^polls/$', 'polls.views.index'),5�_�                            ����                                                                                                                                                                                                                                                                                                                                                  V        Rr     �                    # Examples:   :    # url(r'^$', 'mercenaryLair.views.home', name='home'),   A    # url(r'^mercenaryLair/', include('mercenaryLair.foo.urls')),       G    # Uncomment the admin/doc line below to enable admin documentation:   D    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),       2    # Uncomment the next line to enable the admin:5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       Ru     �                .    url(r'^admin/', include(admin.site.urls)),5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       Rw     �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       Ry     �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       R{     �                 5�_�      !                    ����                                                                                                                                                                                                                                                                                                                                                V       R     �                 .    url(r'^admin/', include(admin.site.urls)),5�_�      #           !          ����                                                                                                                                                                                                                                                                                                                                                V       R�     �                 9urlpatterns += url(r'^admin/', include(admin.site.urls)),5�_�   !   $   "       #          ����                                                                                                                                                                                                                                                                                                                                                V       R�     �                 Furlpatterns += patterns('', url(r'^admin/', include(admin.site.urls)),5�_�   #   %           $           ����                                                                                                                                                                                                                                                                                                                                                V       R�     �                 urlpatterns += patterns('',    .    url(r'^admin/', include(admin.site.urls)),�                 .    url(r'^admin/', include(admin.site.urls)),5�_�   $   )           %          ����                                                                                                                                                                                                                                                                                                                                                V       R�     �               urlpatterns = patterns('',5�_�   %   +   (       )           ����                                                                                                                                                                                                                                                                                                                                                V       R�    �   
             ?    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'polls.views.vote'),�   	             E    url(r'^polls/(?P<poll_id>\d+)/results/$', 'polls.views.results'),�      
          <    url(r'^polls/(?P<poll_id>\d+)/$', 'polls.views.detail'),�      	          *    url(r'^polls/$', 'polls.views.index'),5�_�   )   ,   *       +          ����                                                                                                                                                                                                                                                                                                                                                V       R    �                     �               5�_�   +   -           ,   	        ����                                                                                                                                                                                                                                                                                                                            	                      V        R�     �      	          0    url(r'^polls/(?P<poll_id>\d+)/$', 'detail'),   9    url(r'^polls/(?P<poll_id>\d+)/results/$', 'results'),   3    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'vote'),5�_�   ,   .           -          ����                                                                                                                                                                                                                                                                                                                            	           	           V        R�     �      	             url(r'^polls/$', 'index'),5�_�   -   /           .          ����                                                                                                                                                                                                                                                                                                                            	           	           V        R    �      	         +    url(r'^polls/$', include('polls.urls'),5�_�   .   0           /          ����                                                                                                                                                                                                                                                                                                                            	           	           V        R     �               %urlpatterns = patterns('polls.views',5�_�   /   1           0   
        ����                                                                                                                                                                                                                                                                                                                            	           	           V        R"     �   	   
          urlpatterns += patterns('',5�_�   0   2           1   	       ����                                                                                                                                                                                                                                                                                                                            	           	           V        R$     �      	              )5�_�   1   3           2   	        ����                                                                                                                                                                                                                                                                                                                            	           	           V        R&     �   	                 )�      
          .    url(r'^admin/', include(admin.site.urls)),5�_�   2   4           3   	       ����                                                                                                                                                                                                                                                                                                                            	           	           V        R,     �      
   
      0      url(r'^admin/', include(admin.site.urls)),5�_�   3   5           4   
       ����                                                                                                                                                                                                                                                                                                                            	           	           V        R/     �   	                    )5�_�   4   6           5           ����                                                                                                                                                                                                                                                                                                                                       	           V        R5     �      
   
      *    url(r'^polls/', include('polls.urls'),   .    url(r'^admin/', include(admin.site.urls)),5�_�   5   7           6   
        ����                                                                                                                                                                                                                                                                                                                                       	           V        R9   	 �   	              )    �   
                �   
            5�_�   6   8           7      '    ����                                                                                                                                                                                                                                                                                                                                                             R�    �      	   
      (  url(r'^polls/', include('polls.urls'),5�_�   7   9           8          ����                                                                                                                                                                                                                                                                                                                                                             RB�    �      	   
      )  url(r'^polls/', include('polls.urls')),5�_�   8   :           9      &    ����                                                                                                                                                                                                                                                                                                                                                             RB�    �      	   
      /  url(r'^display.php/', include('polls.urls')),5�_�   9   ;           :           ����                                                                                                                                                                                                                                                                                                                                                  V        R�     �      
   
    5�_�   :   <           ;   	       ����                                                                                                                                                                                                                                                                                                                                                  V        R�     �      
         1  url(r'^display.php/', include('display.urls')),5�_�   ;   =           <   	   
    ����                                                                                                                                                                                                                                                                                                                                                  V        R�     �      
         &  url(r'^/', include('display.urls')),5�_�   <   >           =          ����                                                                                                                                                                                                                                                                                                                                                  V        R�    �      	         1  url(r'^display.php/', include('display.urls')),5�_�   =   ?           >           ����                                                                                                                                                                                                                                                                                                                                                             R�     �   
             )�   	             ,  url(r'^admin/', include(admin.site.urls)),�      
          %  url(r'^', include('display.urls')),�      	          0  url(r'^display.php', include('display.urls')),5�_�   >   A           ?   	        ����                                                                                                                                                                                                                                                                                                                            	           	           V        R�     �      	          '    url(r'^', include('display.urls')),5�_�   ?       @       A   	       ����                                                                                                                                                                                                                                                                                                                            	           	           V        R�    �   	      
    5�_�   ?           A   @   
       ����                                                                                                                                                                                                                                                                                                                            	           	           V        R�     �   
             '    url(r'^', include('display.urls')),5�_�   )           +   *          ����                                                                                                                                                                                                                                                                                                                                                V       R     �                5�_�   %       '   )   (           ����                                                                                                                                                                                                                                                                                                                                                V       R�     �                urlpatterns = patterns(',�      	              url(r'^polls/$', 'index'),�      
          0    url(r'^polls/(?P<poll_id>\d+)/$', 'detail'),�   	             9    url(r'^polls/(?P<poll_id>\d+)/results/$', 'results'),�   
             3    url(r'^polls/(?P<poll_id>\d+)/vote/$', 'vote'),5�_�   %       &   (   '           ����                                                                                                                                                                                                                                                                                                                                                V       R�     �      	              url(r'^polls/$', '.index'),�      
          1    url(r'^polls/(?P<poll_id>\d+)/$', '.detail'),�   	             :    url(r'^polls/(?P<poll_id>\d+)/results/$', '.results'),�   
             4    url(r'^polls/(?P<poll_id>\d+)/vote/$', '.vote'),5�_�   %           '   &           ����                                                                                                                                                                                                                                                                                                                                                V       R�     �                urlpatterns = patterns('.,�      	              url(r'^polls/$', '.index'),�      
          1    url(r'^polls/(?P<poll_id>\d+)/$', '.detail'),�   	             :    url(r'^polls/(?P<poll_id>\d+)/results/$', '.results'),�   
             4    url(r'^polls/(?P<poll_id>\d+)/vote/$', '.vote'),5�_�   !           #   "          ����                                                                                                                                                                                                                                                                                                                                                V       R�     �                urlpatterns += patterns('',   ?    lllllllllllllllllurl(r'^admin/', include(admin.site.urls)),5�_�              !          8    ����                                                                                                                                                                                                                                                                                                                                                V       R�     �                8urlpatterns += url(r'^admin/', include(admin.site.urls))5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       R|     �                *url(r'^admin/', include(admin.site.urls)),�                /    )url(r'^admin/', include(admin.site.urls)),5�_�                           ����                                                                                                                                                                                                                                                                                                                                                       R�     �                                 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       R��     �              5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             R��     �               /    u rl(r'^admin/', include(admin.site.urls)),5��