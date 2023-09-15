import cassiopeia as cass
import requests
import customtkinter
from PIL import Image
from PIL import ImageTk
from io import BytesIO
import tkinter


def remake_check(t) :
   if t==True: 
       return "Remake"
   else :
       return False
def win_check(t):
   if t==True: 
       return "Victory"
   else :
       return 'Defeat'     
def laneRole(role):
     if role=='utility':
         return 'Support'
     elif role=='bot_lane':
         return 'ADC'
     elif role=='top_lane':
         return 'Top Lane'
     elif  role=='mid_lane':
         return 'Mid Lane'
     elif role=='jungle':
         return 'Jungle'
     else:
         return 'ARAM'
       

cass.set_riot_api_key("RGAPI-e3c8caca-8421-4a91-bb2d-4bceac933b8e")

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("dark-blue")
class App(customtkinter.CTk):

    WIDTH = 1350
    HEIGHT = 900
    
    def __init__(self):
        super().__init__()
        self.title("Data from LoL.py")
        self.geometry(f"{App.WIDTH}x{App.HEIGHT}")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)  
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame_left = customtkinter.CTkFrame(master=self,
                                                 width=180,
                                                 corner_radius=0)
        self.frame_left.grid(row=0, column=0, sticky="nswe")

        self.frame_right = customtkinter.CTkFrame(master=self)
        self.frame_right.grid(row=0, column=1, sticky="nswe", padx=20, pady=20)

        # ============ frame_left ============

        
        self.frame_left.grid_rowconfigure(0, minsize=10) 
        self.frame_left.grid_rowconfigure(7, weight=1)  
        self.frame_left.grid_rowconfigure(8, minsize=20)    
        self.frame_left.grid_rowconfigure(11, minsize=10) 

        self.label_1 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Data from LoL",
                                              text_font=("Roboto Medium", -20))  
        self.label_1.grid(row=1, column=0, pady=10, padx=10)
        self.label_2 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Insert Summoner Name:",
                                              text_font=("Roboto Medium", -16)) 
        self.label_2.grid(row=2, column=0, pady=10, padx=10)
        self.enter_1 = customtkinter.CTkEntry(master=self.frame_left)
        self.enter_1.grid(row=3, column=0, pady=5, padx=5)
        self.label_3 = customtkinter.CTkLabel(master=self.frame_left,
                                              text="Insert Region:",
                                              text_font=("Roboto Medium", -16))  
        self.label_3.grid(row=4, column=0, pady=10, padx=10)
        self.enter_2 = customtkinter.CTkEntry(master=self.frame_left)
        self.enter_2.grid(row=5, column=0, pady=5, padx=5)
        
        self.button_1 = customtkinter.CTkButton(master=self.frame_left,
                                                 text="Search",
                                                 command=self.button_event)
        self.button_1.grid(row=6, column=0, pady=10, padx=20)

        self.label_mode = customtkinter.CTkLabel(master=self.frame_left, text="Appearance Mode:")
        self.label_mode.grid(row=9, column=0, pady=0, padx=20, sticky="w")

        self.optionmenu_1 = customtkinter.CTkOptionMenu(master=self.frame_left,
                                                        values=["Dark","Light"],
                                                        command=self.change_appearance_mode)
        self.optionmenu_1.grid(row=10, column=0, pady=10, padx=20, sticky="w")

        # ============ frame_right ============

        
        self.frame_right.rowconfigure((0), weight=1)
        
        self.frame_right.columnconfigure((0), weight=1)
        
        
        self.frame_info = customtkinter.CTkFrame(master=self.frame_right)
        self.frame_info.columnconfigure((0,1,2,3,4,5,6), weight=1)
        self.frame_info.grid(row=0, column=0, columnspan=2, rowspan=4, pady=20, padx=20, sticky="nsew")

          

       
        self.ATT1 = customtkinter.CTkLabel(master=self.frame_left,
                                             text="",text_font=("Roboto Medium", -14)
                                             )
        self.ATT1.grid(row=7, column=0, pady=10, padx=20)
    
        
    def button_event(self):
        
        
        summoner = cass.get_summoner(name=self.enter_1.get(),region=self.enter_2.get())
        ex=summoner.exists
        if ex==False:
            
            self.ATT1.configure(text="Invalid user please check and try again",text_font=("Roboto Medium", -14))
        else:
        
            
            cleanRegion=str(summoner.region).partition('.')[2].replace('_',' ')
            self.label_info_1=customtkinter.CTkLabel(master=self.frame_info,
                                                       text='{name}\nLevel: {level}\nRegion: {region}'.format(name=summoner.name,level=summoner.level,region=cleanRegion.title()),
                                                       text_font=("Roboto Medium", -16),height=100,
                                                       corner_radius=6,  
                                                       fg_color=("gray38"),  
                                                       justify=tkinter.LEFT)
            self.label_info_1.grid(column=1, row=0, sticky="nwe",padx=15,pady=15)
            
            pic=summoner.profile_icon
            url='https://ddragon.leagueoflegends.com/cdn/12.22.1/img/profileicon/'+str(pic.id)+'.png' 
            r = requests.get(url)
            pilImage = Image.open(BytesIO(r.content))
            
            pilImage=pilImage.resize((100, 100))
            icon=ImageTk.PhotoImage(pilImage)
            self.iconLbl=customtkinter.CTkLabel(master=self.frame_info,image=icon,corner_radius=6)
            self.iconLbl.image=icon
            
            self.iconLbl.grid(column=0, row=0, sticky="ew",padx=15, pady=15)
            self.duration=customtkinter.CTkLabel(master=self.frame_info,text='Match', text_font=("Roboto Medium", -28))
            self.duration.grid(column=0, row=1, sticky="ew",padx=15,pady=15)
            self.duration=customtkinter.CTkLabel(master=self.frame_info,text='Result', text_font=("Roboto Medium", -28))
            self.duration.grid(column=1, row=1, sticky="ew",padx=15,pady=15)
            self.duration=customtkinter.CTkLabel(master=self.frame_info,text='Champion', text_font=("Roboto Medium", -28))
            self.duration.grid(column=2, row=1, sticky="ew",padx=15,pady=15)
            self.duration=customtkinter.CTkLabel(master=self.frame_info,text='KDA', text_font=("Roboto Medium", -28))
            self.duration.grid(column=3, row=1, sticky="ew",padx=15,pady=15)
            self.duration=customtkinter.CTkLabel(master=self.frame_info,text='CS & Gold', text_font=("Roboto Medium", -28))
            self.duration.grid(column=4, row=1, sticky="ew",padx=15,pady=15)
            self.duration=customtkinter.CTkLabel(master=self.frame_info,text='Vision', text_font=("Roboto Medium", -28))
            self.duration.grid(column=5, row=1, sticky="ew",padx=15,pady=15)
            
            
            
            i=2
            history=summoner.match_history
            champion_id_to_name_mapping = {champion.id: champion.name for champion in cass.get_champions(region=summoner.region)}
            champion_id_to_name_image = {champion.id: champion.key for champion in cass.get_champions(region=summoner.region)}
               
            for Match in history[:7]:
                rawQ=str(Match.queue)
                que=rawQ.partition('.')[2]
                mode=que.replace('_',' ')
                mode=mode.replace('fives','5v5')
                
                p=Match.participants[summoner]
                if mode!='aram':
                    pos=str(p.lane).partition('.')[2]
                    role=laneRole(pos)
                else:
                    role=''
                duration=str(Match.duration)
                
                
                date=str(Match.start).partition('T')[0]
                
                self.label2=customtkinter.CTkLabel(master=self.frame_info,text=mode.title()+'\n'+role+"\nDuration: "+duration+'\n'+date, text_font=("Roboto Medium", -14))
                self.label2.grid(column=0, row=i, sticky="ew",padx=15,pady=15)
            
                champion_id = Match.participants[summoner].champion.id
                
                champion_image= champion_id_to_name_image[champion_id]
                
                champion_name = champion_id_to_name_mapping[champion_id]  
                url2='http://ddragon.leagueoflegends.com/cdn/12.22.1/img/champion/'+str(champion_image)+'.png'
                r2 = requests.get(url2)
                pilImage2 = Image.open(BytesIO(r2.content)) 
                pilImage2=pilImage2.resize((50, 50), Image.ANTIALIAS)
                champion_square=ImageTk.PhotoImage(pilImage2)
                
                
                self.label4=customtkinter.CTkLabel(master=self.frame_info,image=champion_square,text=str(champion_name),compound='top',text_font=("Roboto Medium", -12))
                
                self.label4.grid(column=2, row=i, sticky="ew",padx=15,pady=15)
                self.label4.image=champion_square
                
                
                re=remake_check(Match.is_remake)
                if re==False:
                    outcome=win_check(p.stats.win)
                    if outcome=='Victory':
                        self.win=customtkinter.CTkLabel(master=self.frame_info,text=outcome, text_font=("Roboto Medium", -18),text_color='Green')
                        self.win.grid(column=1, row=i, sticky="ew",padx=15,pady=15)
                    else:
                        self.win=customtkinter.CTkLabel(master=self.frame_info,text=outcome, text_font=("Roboto Medium", -18),text_color='Red')
                        self.win.grid(column=1, row=i, sticky="ew",padx=15,pady=15)
                else:
                    outcome=re
                    self.win=customtkinter.CTkLabel(master=self.frame_info,text=outcome, text_font=("Roboto Medium", -18),text_color='Gray')
                    self.win.grid(column=1, row=i, sticky="ew",padx=15,pady=15)
                    
               
              
    
                
    
                
                Kills=str(p.stats.kills)
                Deaths=str(p.stats.deaths)
                Asists=str(p.stats.assists)
                KDA=f'{p.stats.kda:.2f}'
                
                    
                
                
                self.kda=customtkinter.CTkLabel(master=self.frame_info,text=Kills+'/'+Deaths+'/'+Asists+'\nKDA: '+KDA, text_font=("Roboto Medium", -16))
                self.kda.grid(column=3, row=i, sticky="ew",padx=15,pady=15)
                
                
                gold=str(p.stats.gold_earned)
                minion=((p.stats.total_minions_killed)+(p.stats.neutral_minions_killed))
                cs=str(minion)
                
                
                
                self.grind=customtkinter.CTkLabel(master=self.frame_info,text=cs+' CS\n\nG: '+gold, text_font=("Roboto Medium", -16))
                self.grind.grid(column=4, row=i, sticky="ew",padx=15,pady=15)
                
                
                vision=str(p.stats.vision_score)
                self.grind2=customtkinter.CTkLabel(master=self.frame_info,text=vision, text_font=("Roboto Medium", -16))
                self.grind2.grid(column=5, row=i, sticky="ew",padx=15,pady=15)
                
                
                
                
                
                i=i+1
   


    def change_appearance_mode(self, new_appearance_mode):
            customtkinter.set_appearance_mode(new_appearance_mode)
  
    def on_closing(self, event=0):
            self.destroy()
        
        
if __name__ == "__main__":
     app = App()
     app.mainloop()
      
