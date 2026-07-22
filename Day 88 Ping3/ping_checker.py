from ping3 import ping


def check_host(host):
    try:
        response = ping(host, timeout=2)

        if response is None:
            print(f"\n❌ {host} is unreachable.")
        else:
            print(f"\n✅ {host} is reachable.")
            print(f"Response Time: {round(response * 1000, 2)} ms")

    except Exception as e:
        print(f"\nError: {e}")


def main():
    print("=" * 40)
    print("      WEBSITE PING CHECKER")
    print("=" * 40)

    while True:
        host = input("\nEnter Website/IP: ").strip()

        check_host(host)

        choice = input("\nCheck another? (y/n): ").lower()

        if choice != "y":
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    main()