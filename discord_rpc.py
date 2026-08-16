import discord
from typing import Optional, Dict

class DiscordRPC:
    """Discord Rich Presence を管理"""
    
    def __init__(self, client: discord.Client):
        self.client = client

    async def update_presence(self, roblox_info: Optional[Dict]):
        """
        Discord Rich Presence を更新
        
        Args:
            roblox_info: Robloxゲーム情報
        """
        try:
            if roblox_info:
                # Robloxをプレイ中
                await self.set_roblox_presence(roblox_info)
            else:
                # どちらもアクティブでない場合
                await self.set_idle_presence()
        
        except Exception as e:
            print(f"❌ Discord Presence Error: {e}")

    async def set_roblox_presence(self, game_info: Dict):
        """Robloxプレイ中のプレゼンスを設定"""
        try:
            activity = discord.Activity(
                type=discord.ActivityType.playing,
                name=f"🎮 {game_info.get('game_name', 'Roblox')}",
                details=f"Game ID: {game_info.get('game_id')}",
                state="Playing on Roblox",
                large_image="roblox",
                large_text="Roblox",
                small_image="roblox_small",
                small_text=game_info.get('game_name', 'Roblox')
            )
            
            await self.client.change_presence(activity=activity)
            
        except Exception as e:
            print(f"❌ Roblox Presence Error: {e}")

    async def set_idle_presence(self):
        """アイドル状態のプレゼンスを設定"""
        try:
            activity = discord.Activity(
                type=discord.ActivityType.playing,
                name="🎮 Game Presence Tracker",
                state="Ready to track"
            )
            
            await self.client.change_presence(activity=activity)
            
        except Exception as e:
            print(f"❌ Idle Presence Error: {e}")

    async def set_custom_presence(self, activity_type: discord.ActivityType, name: str, state: str = "", details: str = ""):
        """カスタムプレゼンスを設定"""
        try:
            activity = discord.Activity(
                type=activity_type,
                name=name,
                state=state,
                details=details
            )
            
            await self.client.change_presence(activity=activity)
            
        except Exception as e:
            print(f"❌ Custom Presence Error: {e}")
