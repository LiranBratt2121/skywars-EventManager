from api.hypixel_api import MinecraftStatsFetcher


def main():
    api = MinecraftStatsFetcher()
    username = input("Enter the Minecraft username: ")
    try:
        uuid = api.get_uuid(username)
        skywars_data = api.get_skywars_data(uuid)
        print(skywars_data)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()