from discord.ext import commands

class words(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def words(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('このコマンドにはサブコマンドが必要です。\n以下にコマンドリストを示します')
            await ctx.send('-morning(引数なし)\n-night(引数なし)\n-customer(誰)\n-genius(誰)\n-sumo(誰)\n-car(誰の何が何なのか何がなんなのか)\n-cute(何が、それは何、どうして)')

    @words.command()
    async def morning(self, ctx):
        await ctx.send("おはよー！！！カンカンカン！！！起きて！！！朝だよ！！！！すごい朝！！！！外が明るい！！カンカンカンカンカン！！！！！おはよ！！カンカンカン！！！見て見て！！！！外明るいの！！！外！！！！見て！！カンカンカンカンカン！！起きて！！早く起きて！！カンカン！")

    @words.command()
    async def night(self, ctx):
        await ctx.send('おやすみー………シーンシーンシーン………寝て………夜だよ…………すごい夜…………外が暗い……シーンシーンシーンシーンシーン……………おやすみ……シーンシーンシーン………見なくていいけど…………外暗いの………外…………見るくらいなら寝て……シーンシーンシーンシーンシーン……寝て……早く寝て……シーンシーン…')

    @words.command()
    async def customer(self, ctx, who):
        await ctx.send(f'困ります！！困ります！！{who}！！困ります！！あーっ！！困ります！！{who}！！あーっ！！{who}！！{who}！！{who}困り！！あーっ{who}！！困りますあーっ！！困ーっ！！{who[0:-2]}困ーっ！！困ります！！困り{who[-1]}！！あーっ！！{who}！！困ります！！困ります！！{who[0:-2]}ます！！あーっ！！{who}！！')

    @words.command()
    async def genius(self, ctx, who):
        await ctx.send(f'{who}では長いですから✞天才✞とお呼びください')

    @words.command()
    async def sumo(self,ctx,who):
        await ctx.send(f'あ❗{who}❗🌚ダン💥ダン💥ダン💥シャーン🎶{who[0]}{who[-1]}🌝{who[0:1]}🌚{who[0]}{who[-1]}🌝{who[0]}{who[-1]}🌝{who[0:1]}🌝{who[0]}{who[-1]}🌝{who[0]}{who[-1]}🌝{who[0:1]}🌚{who[0]}{who[-1]}🌝{who[0]}{who[-1]}🌝{who[0:1]}🌝{who[0]}{who[-1]}🌝{who[0:1]}🌚{who[0:1]}～～{who[1:]}⤴🌝{who[0]}{who[-1]}🌝{who[0:1]}🌚{who[0]}{who[-1]}🌝{who[0:1]}🌝{who[0]}{who[-1]}🌝{who[0:1]}🌚{who[0]}{who[-1]}🌝{who[0:1]}🌝{who[0]}{who[-1]}🌝{who[0]}{who[-1]}🌝{who[0:1]}🌚{who[0]}{who[-1]}🌝{who[0]}{who[-1]}🌝{who[0:1]}🌝{who[0:1]}～～{who[1:]}⤵🌞')

    @words.command()
    async def car(self,ctx ,who, what ,what2,what3,how):
        await ctx.send(f'{who}の{what}が{what2}でした。死にたいくらい恥ずかしくて惨めな思いのデートでした。\n{what2}とかないですよね。\nしかも{what3}とか「{how}かよ」って感じですｗ\nあたし何かおかしいこと言ってますか？\n普通の感覚ですよね？')

    @words.command()
    async def cute(self,ctx,who,whod,what):
        await ctx.send(f'                       ₍₍⁽⁽{who}₎₎⁾⁾')
        await ctx.send(f'見て！{whod}が踊っているよ\nかわいいね\n\n')
        await ctx.send(f'                           {who}')
        await ctx.send(f'{what}ので、{whod}は踊るのをやめてしまいました\nお前のせいです\nあ〜あ')

def setup(bot):
    bot.add_cog(words(bot))