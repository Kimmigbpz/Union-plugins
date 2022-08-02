# -*- coding: utf-8 -*-
# made by GBPZkimmi
# v1.3 2022/8/2
PLUGIN_METADATA = {
    'id': 'Union plugins',
    'version': '0.1.3',
    'name': 'Union plugins',
    'link': 'https://github.com/hanbings/ConfigAPI'
}
def on_load(server):
    server.register_help_message('!!dim true/false', '开启或关闭服务器超线程优化')
    server.register_help_message('!!mcdr lvl', '查看自己MCDR的等级')
    server.register_help_message('!!tick', '对服务器游戏刻进行控制{开发中,仅限制MCDR 2等级及以上}')
    server.register_help_message('*#*#*#', '还有一些彩蛋需要自己发掘哦')
    
def on_info(server,info):
    
    if info.is_player:
        if info.content.split == '!!dim':
            server.say('!!dim true 开启服务器超线程优化\n!!dim false 关闭服务器超线程优化')
        elif info.content.split == '!!dim true':
            server.execute('gamerule dimthread_active true')
            server.say('多线程优化已开启')
        elif info.content.split == '!!dim false':
            server.execute('gamerule dimthread_active false')
            server.say('多线程优化已关闭')
        elif info.content == '!!kill':
            server.execute('kill ' + info.player)
            server.say('嘿嘿嘿，你被腐竹刻意的设计杀死了')
        elif info.content == 'shit':
            server.say('小伙子，年纪轻轻要心平气和')
        elif info.content == '!!ban':
            server.say('NAN')
        elif info.content == '!!pardon':
            server.say('NAN')
        elif info.content == '!!mcdr lvl':
            server.say("玩家：" + info.player + "您的MCDR等级是" + str(server.get_permission_level(info.player)))
            if server.get_permission_level(info.player) == 2:
                server.say("等级2为helper，属服务器重要成员，可以进行一些关键指令操作")
            elif server.get_permission_level(info.player) == 1:
                server.say("等级1为player，属服务器普通成员，可以进行所有基本操作，以及一些特殊操作")
            elif server.get_permission_level(info.player) == 3:
                server.say("等级3为admin，属服务器管理员，可以进行所有插件与指令操作，但不会破坏游戏平衡")
            elif server.get_permission_level(info.player) == 4:
                server.say("等级4为owner，属服务器所有者，可以进行所有插件与指令操作与调试，但不会破坏游戏平衡")
            elif server.get_permission_level(info.player) == 0:
                server.say("等级0为guest，属服务器参观者，可以进行所有基本操作，但无法进行任何特殊操作")
        elif info.content == '!!tick':
            args = info.content.split()
            if server.get_permission_level(info.player) >= 2:
                server.say(args[2] + args[3])
                server.say(info.content.split)
                server.say(args)
            else:
                server.say("您无权限超控服务器游戏刻")
    


