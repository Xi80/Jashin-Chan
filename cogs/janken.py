from discord.ext import commands
import random
class janken(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    #チョキ = 0
    #パー = 1
    #グー = 2
    async def on_message(self, message):
        if message.author.bot:
            return

        if str(message.content).find('邪神ちゃんとじゃんけん') != -1:
            if str(message.content).find('チョキで勝つ') != -1 or str(message.content).find('パーで勝つ') != -1 or str(message.content).find('グーで勝つ') != -1:
                if random.randint(0,2) == 1:
                    await message.channel.send('じゃんけんポン！(真顔)')
                    await message.channel.send('YOU WIN(ﾋﾟｭｩｫｵｵｵｵｫｫｫｫ!!!!)')
                    await message.channel.send('すごいなお前！😁')
                    await message.channel.send('明日は俺にリベンジさせろよな！')
                    await message.channel.send('じゃあ、これやるよ(ﾌﾞｼｭｳｳｳｳｳｳｳ)')
                else:
                    await message.channel.send('じゃんけんポン！(真顔)')
                    await message.channel.send('YOU LOSE(ﾌﾞｩｩｩｩｩｩｩ!!!!)')
                    await message.channel.send('俺の勝ち！😁')
                    await message.channel.send('なんで負けたか、明日までに考えておくんだな！')
                    await message.channel.send('じゃあ、いただくぜ(ﾌﾞｼｭｳｳｳｳｳｳｳ)')
def setup(bot):
    bot.add_cog(janken(bot))