import random

import discord
from discord.ext import commands


class Kuji(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @discord.app_commands.command(name="kuji", description="HTTPステータスコードでおみくじを引きます。")
    async def kuji(self, interaction: discord.Interaction) -> None:
        status_codes = {
            100: "100: 継続中 - 小吉\n次のプロジェクトに集中すると吉！",
            200: "200: OK - 大吉\n今日のデプロイは成功する予感！",
            201: "201: 作成されました - 大吉\n新しいプロジェクトが成功する予感！",
            202: "202: 受理されました - 吉\n良い結果が期待できそうです。",
            204: "204: 内容なし - 中吉\nシンプルに行こう！",
            301: "301: 恒久的に移動 - 中吉\n古いコードをリファクタリングしよう！",
            302: "302: 一時的に移動 - 吉\n新しいアイデアを試してみよう！",
            304: "304: 未変更 - 小吉\n現状維持が吉。",
            307: "307: 一時的リダイレクト - 中吉\n一時的な変更が良い結果をもたらすかも。",
            400: "400: 不正なリクエスト - 凶\n計画を見直す必要があるかも。",
            401: "401: 認証が必要 - 小凶\nもう少し努力が必要です。",
            403: "403: 禁止されています - 凶\n今日は控えめに行動しよう。",
            404: "404: 見つかりません - 凶\n探し物が見つからないかも…。",
            405: "405: 許可されていないメソッド - 凶\n計画を見直す必要があるかも。",
            408: "408: リクエストタイムアウト - 凶\n焦らずに行動しよう。",
            409: "409: 競合 - 凶\n衝突を避けるために慎重に行動しよう。",
            410: "410: 消失 - 凶\n過去のことにとらわれず前に進もう。",
            418: "418: 私はティーポット - ユーモア吉\nお茶でも飲んで一息つこう。",
            429: "429: リクエストが多すぎます - 凶\n少し休んでから再挑戦しよう。",
            451: "451: 法的理由により利用不可 - 凶\n今日は慎重に行動しよう。",
            500: "500: サーバーエラー - 大凶\n今日は無理をしないで！",
            502: "502: 不正なゲートウェイ - 大凶\n今日はトラブルに注意！",
            503: "503: サービス利用不可 - 大凶\n今日は休息が必要です。",
            504: "504: ゲートウェイタイムアウト - 凶\n焦らずに行動しよう。",
            511: "511: ネットワーク認証が必要 - 小凶\nもう少し努力が必要です。",
            206: "206: 部分的なコンテンツ - 吉\n部分的な成功が期待できそうです。",
            207: "207: 複数のステータス - 中吉\n複数の良い結果が期待できそうです。",
            226: "226: IM使用 - 吉\n新しい技術を試してみよう！",
            308: "308: 永続的リダイレクト - 中吉\n長期的な変更が良い結果をもたらすかも。",
            402: "402: 支払いが必要 - 凶\n予算を見直す必要があるかも。",
            406: "406: 受理できません - 凶\n計画を再考する必要があるかも。",
            407: "407: プロキシ認証が必要 - 小凶\nもう少し努力が必要です。",
            412: "412: 前提条件失敗 - 凶\n計画を見直す必要があるかも。",
            413: "413: ペイロードが大きすぎます - 凶\n計画を見直す必要があるかも。",
            414: "414: URIが長すぎます - 凶\n計画を見直す必要があるかも。",
            415: "415: サポートされていないメディアタイプ - 凶\n計画を見直す必要があるかも。",
            416: "416: 範囲外のリクエスト - 凶\n計画を見直す必要があるかも。",
            417: "417: 期待失敗 - 凶\n計画を見直す必要があるかも。",
            421: "421: 誤ったリクエスト - 凶\n計画を見直す必要があるかも。",
            422: "422: 処理できないエンティティ - 凶\n計画を見直す必要があるかも。",
            423: "423: ロックされています - 凶\n計画を見直す必要があるかも。",
            424: "424: 依存関係の失敗 - 凶\n計画を見直す必要があるかも。",
            426: "426: アップグレードが必要 - 凶\n計画を見直す必要があるかも。",
            428: "428: 前提条件が必要 - 凶\n計画を見直す必要があるかも。",
            431: "431: ヘッダーが大きすぎます - 凶\n計画を見直す必要があるかも。",
            444: "444: 接続が閉じられました - 凶\n計画を見直す必要があるかも。",
            499: "499: クライアントが閉じました - 凶\n計画を見直す必要があるかも。",
            505: "505: HTTPバージョンがサポートされていません - 凶\n計画を見直す必要があるかも。",
            506: "506: バリアントも交渉します - 凶\n計画を見直す必要があるかも。",
            507: "507: ストレージ不足 - 凶\n計画を見直す必要があるかも。",
            508: "508: ループ検出 - 凶\n計画を見直す必要があるかも。",
            510: "510: 拡張が必要 - 凶\n計画を見直す必要があるかも。"
        }
        code = random.choice(list(status_codes.keys()))
        embed = discord.Embed(title="HTTP Status Kuji", description=status_codes[code], color=discord.Color.blue())
        await interaction.response.send_message(embed=embed)


async def setup(bot):
    await bot.add_cog(Kuji(bot))
