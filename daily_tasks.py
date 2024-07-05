from utils.gamepad.gamepad_controller import *
from controller.target_detector import *
from start_game import *
from utils.general_processor.handler import random_sleep,wait_page_by_text,findText_with_full_Text,get_screenshot

class DailyTask:
    def __init__(self, window ,pigeon = print):
        self.gp = Gamepad(pigeon = pigeon)
        self.pigeon = pigeon
        try:
            self.window = gw.getWindowsWithTitle("崩坏：星穹铁道")[0]
        except:
            self.window = None
            self.start_game()
            self.window = gw.getWindowsWithTitle("崩坏：星穹铁道")[0]
    def start_game(self):
        SG = StartGame(pigeon= self.pigeon,gp = self.gp)
        self.pigeon("start game with gamepad")
        SG.start_game()

    def open_nameless_honor(self):
        # 打开勋礼页面
        self.gp.press_button(LEFT_SHOULDER)
        self.gp.joystick_movement(np.pi * 3 / 4)
        random_sleep(0.8)
        self.gp.joystick_movement(amplitude=0)
        self.gp.release_button(LEFT_SHOULDER)
        random_sleep(1)
                
        figure,_,_,_,_ = get_screenshot(self.window)
        find,_,_ = findText_with_full_Text(figure,text = "无名勋礼")
        if find:
            self.pigeon("勋礼已经打开")
        else:
            self.gp.press_button(B)
            random_sleep(0.3)
            self.gp.press_button(B)
            random_sleep(0.3)
            self.gp.press_button(B)
            random_sleep(0.3)
            self.open_star_guide()
        # self.pigeon("打开星际和平指南")
        random_sleep(0.9)

    # 无名勋礼
    def get_nameless_honor(self):
        # 打开勋礼页面
        self.open_nameless_honor()

        # 已经打开后，通过手柄切换标签找到对应的page
        if TargetDetector(self.window,self.gp).search_button("任务", RIGHT_SHOULDER):
            self.pigeon("找到：任务")
        else:
            self.pigeon("未找到：任务")
        # 切换到领取页面
        # self.gp.click_button(RIGHT_SHOULDER)
        random_sleep(0.1)
        self.gp.click_button(Y)
        random_sleep(0.1)
        # 已经打开后，通过手柄切换标签找到对应的page
        if TargetDetector(self.window,self.gp).search_button("奖励", LEFT_SHOULDER):
            self.pigeon("找到：奖励")
        else:
            self.pigeon("未找到：奖励")
        random_sleep(0.1)
        self.gp.click_button(Y)

        # 离开页面
        random_sleep(0.1)
        self.gp.click_button(B)
        random_sleep(0.1)
        self.gp.click_button(B)
        random_sleep(0.1)
        self.gp.click_button(B)
        random_sleep(0.1)

    def find_page(self,tag = "生存索引"):
        # self.pigeon("开始寻找 "+tag)
        # 已经打开星际和平指南后，通过手柄切换标签找到对应的page
        if TargetDetector(self.window,self.gp).search_button(tag, RIGHT_SHOULDER):
            self.pigeon("找到" + tag)
        else:
            self.pigeon("未找到" + tag)

    def find_type(self,  type = "遗器"):
        # 已经找好了目标page，去仔细找对应的类型，如模拟宇宙、拟造花萼等
        if TargetDetector(self.window,self.gp).find_highlight(type, DOWN):
            self.pigeon("找到" + type)
        else:
            self.pigeon("未找到" + type)
        pass

    def find_dungeon(self, dungeon):
        # 已经找好了目标page，去仔细找对应的类型，如模拟宇宙、拟造花萼等
        self.gp.click_button(A)
        if TargetDetector(self.window,self.gp).find_dungeon(dungeon, DOWN):
            self.pigeon("找到" + dungeon)
        else:
            self.pigeon("未找到目标")
        pass



    def open_star_guide(self):
        # 打开星际和平指南
        self.gp.press_button(LEFT_SHOULDER)
        self.gp.joystick_movement(np.pi * 1 / 4, duration= 1) # 移动到指南
        random_sleep(0.8)
        self.gp.joystick_movement(amplitude=0)
        self.gp.release_button(LEFT_SHOULDER)
        
        random_sleep(1)
        figure,_,_,_,_ = get_screenshot(self.window)
        find,_,_ = findText_with_full_Text(figure,text = "星际和平指南")
        if find:
            self.pigeon("和平指南已经打开")
        else:
            self.gp.press_button(B)
            random_sleep(0.3)
            self.gp.press_button(B)
            random_sleep(0.3)
            self.gp.press_button(B)
            random_sleep(0.3)
            self.open_star_guide()
        # self.pigeon("打开星际和平指南")
        random_sleep(0.9)

    def check_stamina(self):
        # 检查体力
        screenshot,_,_,_,_ = get_screenshot(self.window)
        _,_,fullText = findText_with_full_Text(screenshot,r"/240")
        stamina = fullText.split(r'/')
        self.pigeon("体力：" + stamina[0] + "/" + stamina[1])
        return int(stamina[0])
    
    def little_dungeon_10(self,farm_list):
        '''
        
        '''
        self.find_page("生存索引") # 生存索引页
        random_sleep()
        
        """10体力小本"""
        if farm_list[0] == 0:
            # 花萼金
            self.find_type("经验材料/信用点")
            if farm_list[1] == 0:
                # 经验本
                self.pigeon("经验书")
                self.find_dungeon("回忆") # 自带按下A了
                random_sleep()
            if farm_list[1] == 1:
                # 武器本
                self.pigeon("武器经验")
                self.find_dungeon("以太") # 自带按下A了
                random_sleep()
            if farm_list[1] == 2:
                # 武器本
                self.pigeon("信用点")
                self.find_dungeon("藏珍") # 自带按下A了
                random_sleep()
        if farm_list[0] == 1:
            # 花萼赤，直接把text传进来比较好
            self.find_type("行迹材料")
            # if farm_list[1] == 0:
            self.pigeon(farm_list[1])
            if farm_list[1] == 0:
                self.find_dungeon("收容")
            if farm_list[1] == 1:
                self.find_dungeon("鳞渊")
            if farm_list[1] == 2:
                self.find_dungeon("支援舱段")
            if farm_list[1] == 3:
                self.find_dungeon("克劳克影视乐园")
            if farm_list[1] == 4:
                self.find_dungeon("城郊雪原")
            if farm_list[1] == 5:
                self.find_dungeon("苏乐达")
            if farm_list[1] == 6:
                self.find_dungeon("边缘通路")
            if farm_list[1] == 7:
                self.find_dungeon("绥园")
            if farm_list[1] == 8:
                self.find_dungeon("铆钉镇")
            if farm_list[1] == 9:
                self.find_dungeon("机械聚落")
            if farm_list[1] == 10:
                self.find_dungeon("酒店-梦境")
            if farm_list[1] == 11:
                self.find_dungeon("大矿区")
            if farm_list[1] == 12:
                self.find_dungeon("丹鼎司")
            # self.find_dungeon(farm_list[1][-2])
        ## 找到了以后点确定
        self.gp.click_button(A)
        # 等待传送和加载界面
        wait_page_by_text(self.window, "挑战")
        self.pigeon("加载完成")
        self.using_stamina(10)


    def using_stamina(self,stamina_cost,find_tag = "A"):
        stamina = self.check_stamina() # 获取当前体力数值
        # 小本耗10
        count = 0
        if stamina_cost == 10:
            while stamina > 10:
                battle_times = 0
                if stamina > 60:
                    # 拉满，六次扳机
                    battle_times = 6
                else:
                    battle_times = int(np.floor(stamina/10))
                for _ in range(battle_times):
                    self.gp.RIGHT_TRIGGER(1)
                    random_sleep(0.01)
                self.gp.click_button(Y) # 开始，进入编队
                random_sleep(0.5)
                self.gp.click_button(Y) # 开始战斗

                stamina -= battle_times * 10
                wait_page_by_text(self.window, "退出关卡",timeout= 600)
                count += 1
                self.pigeon("完成战斗 "+str(count) + " 次")
                if stamina > 60:
                    self.gp.click_button(Y) # 再来一次
                elif stamina > 10:
                    self.gp.click_button(B) # 推出
                    
                    
                    random_sleep(2)
                    self.gp.click_button(A) # 再进入挑战界面
                else:
                    self.gp.click_button(B) # 推出
        else:
            while stamina > stamina_cost:
                self.gp.click_button(Y) # 开始，进入编队
                random_sleep(0.5)
                self.gp.click_button(Y) # 开始战斗
                random_sleep(0.5)
                self.gp.click_button(X)
                random_sleep(0.5)
                self.gp.click_button(X)
                random_sleep(0.5)
                self.gp.click_button(X) # 确保凝滞虚影能打到怪
                stamina -= stamina_cost
                wait_page_by_text(self.window, "退出关卡",timeout= 600)
                self.gp.click_button(B) # 退出
                count += 1
                self.pigeon("完成战斗 "+str(count) + " 次")
                # random_sleep(5)w

                wait_page_by_text(self.window,find_tag) # wait 多久？
                self.pigeon("find:"+find_tag)
                random_sleep(1)

                self.gp.click_button(A) # 进入副本
                random_sleep(0.5)

        self.pigeon("体力清除完成")
        self.gp.click_button(B) # 进入副本
        random_sleep(0.5)
        self.gp.click_button(B) # 进入副本
        random_sleep(0.3)
        self.gp.click_button(B) # 进入副本
        random_sleep(0.7)
    def illusion(self,name):
        '''
        刷凝滞虚影
        '''
        self.find_type("凝滞虚影")
        self.pigeon("找到凝滞虚影")
        self.find_dungeon(name)
        self.pigeon("找到" + name)
        self.gp.click_button(A)
        wait_page_by_text(self.window, "挑战")
        self.pigeon("加载完成")
        self.using_stamina(30,name)


    def Artifacts(self,name):
        self.find_type("遗器")
        # self.pigeon("找到隧洞")
        self.find_dungeon(name)
        # self.pigeon("找到" + name)
        self.gp.click_button(A)
        wait_page_by_text(self.window, "挑战")
        self.pigeon("加载完成")
        self.using_stamina(40,name)

    def clean_stamina(self,farm_info):
        """清体力"""
        self.window = self.wait_window("崩坏：星穹铁道")
        # self.check_stamina() # 检查有多少体力
        # return
        # 先打开指南
        self.open_star_guide()

        random_sleep(0.5)
        # 
        self.pigeon("寻找生存--索引页面")
        self.find_page("生存索引")
        if farm_info[0] == 0 or farm_info[0] == 1:
            # 花萼
            self.little_dungeon_10(farm_info)
        if farm_info[0] == 2:
            # 凝滞虚影
            self.illusion(farm_info[1])
        if farm_info[0] == 3:
            self.Artifacts(farm_info[1])

    def check_daily_task(self):
        figure,_,_,_,_ = get_screenshot(self.window)
        find,_,_ = findText_with_full_Text(figure,text = "进行中")
        find2,_,_ = findText_with_full_Text(figure,text = "前往")
        if find or find2:
            self.pigeon("仍有进行中日常")
        return find or find2
    
    def daily_task(self):
        # 打开每日实训界面
        self.open_star_guide()
        self.pigeon("寻找实训界面")
        self.find_page("每日实训")

        # 检查今日日常
        find = self.check_daily_task()
        if not find:
            self.pigeon("日常已经全部完成")
            self.gp.click_button(UP)
            random_sleep(0.3)
            self.gp.click_button(A)
            return True
        
        ## 领取所有完成的任务
        figure,_,_,_,_ = get_screenshot(self.window)
        find,_,_ = findText_with_full_Text(figure,text = "领取")
        self.gp.click_button(DOWN)
        random_sleep(0.3)
        while find:
            self.gp.click_button(A)
            random_sleep(0.2)
            figure,_,_,_,_ = get_screenshot(self.window)
            find,_,_ = findText_with_full_Text(figure,text = "领取")

        ## 看看委托？
        finds = TargetDetector(self.window,self.gp).find_daily_weituo()
        if finds[0]:
            # 找到委托tag
            if finds[1]:
                self.pigeon("委托未进行")
                random_sleep(0.5)
                self.gp.click_button(A)
                # 还没进行委托
                random_sleep(0.5)
                figure,_,_,_,_ = get_screenshot(self.window)
                find,_ = findText(figure,text = "一键领取")
                random_sleep(1)
                if find:
                    # 委托可领取
                    self.pigeon("委托可领取")
  
                    random_sleep(1)
                    self.gp.click_button(X)
                    random_sleep(1)
                    self.gp.click_button(Y)
                    random_sleep(1)
                else:
                    # 不可领取
                    self.pigeon("委托不可领取")
                self.gp.click_button(B)
                # 完成重新委托
            else:
                self.pigeon("委托已完成")
        random_sleep(0.2)
        self.gp.click_button(UP)
        random_sleep(0.2)
        self.gp.click_button(UP)
        random_sleep(0.2)
        self.gp.click_button(A)
        random_sleep(0.2)
        self.gp.click_button(A)
        # 离开页面
        for i in range(3):
            random_sleep(0.1)
            self.gp.click_button(B)



    def wait_window(self, game_title):
        timeout = 20  # 等待窗口出现的最大秒数
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                window = gw.getWindowsWithTitle(game_title)[0]
                window.activate()
                return window

            except IndexError:
                # 如果窗口没有找到，继续尝试
                pass
            random_sleep(0.3)  # 等待1秒后再尝试


def main(game_title="崩坏：星穹铁道"):
    window = gw.getWindowsWithTitle(game_title)[0]
    window.activate()
    daily = DailyTask(window)

    # daily.daily_task()
    daily.clean_stamina([3,"药使"])


if __name__ == "__main__":
    main()
