from .. import loader, utils

@loader.tds
class KairoDonateMod(loader.Module):
    """
    💎 Kairo Donate
    Современная донат-панель для Kairo Community
    """

    strings = {"name": "KairoDonate"}

    async def donatecmd(self, message):
        """💸 Показать ссылки для поддержки проекта"""

        text = """
💎 <b>Поддержать Kairo Community</b>

━━━━━━━━━━━━━━━━

🐆 <b>CryptoBot</b>
http://t.me/send?start=IV9bbXjJ7BpD

🐈 <b>TON Keeper</b>
https://app.tonkeeper.com/transfer/UQBfN2p7fr0FaadOXMmCabRKeQrO7609YaxvV7raM0yoD-lm

🔥 <b>Boosty</b>
https://boosty.to/kairorex

━━━━━━━━━━━━━━━━

💸 <i>Каждый донат помогает развитию проекта.</i>

🌸 <b>Спасибо за поддержку!</b>
"""
        await utils.answer(message, text)

    async def donorinfocmd(self, message):
        """📋 Информация о модуле"""

        await utils.answer(
            message,
            """
💎 <b>Kairo Donate V2</b>

⚙️ Команды:
• <code>.donate</code> — панель донатов
• <code>.donorinfo</code> — информация о модуле

🌸 Kairo Community
"""
        )
