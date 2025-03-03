# Simple Prompt Manager
# This program demonstrates basic Python concepts by creating a minimal
# prompt storage and retrieval system using dictionaries.

def main():
    # Initialize an empty list to store prompts
    prompts = []

    while True:
        # Display menu options
        print("\n===== Simple Prompt Manager =====")
        print("1. Add a new prompt")
        print("2. View all prompts")
        print("3. Search prompts")
        print("4. Exit")

        # Get user input
        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            # Add new prompt
            title = input("Enter prompt title: ")
            content = input("Enter prompt content: ")
            topics = input("Enter topics (comma-separated): ").split(",")

            # Clean up topics (remove extra spaces)
            topics = [topic.strip() for topic in topics]

            # Create a prompt dictionary
            prompt = {
                "title": title,
                "content": content,
                "topics": topics
            }

            # Add to our list of prompts
            prompts.append(prompt)
            print("Prompt added successfully!")

        elif choice == "2":
            # View all prompts
            if not prompts:
                print("No prompts found.")
            else:
                print("\n----- All Prompts -----")
                for index, prompt in enumerate(prompts):
                    print(f"\nPrompt #{index + 1}:")
                    print(f"Title: {prompt['title']}")
                    print(f"Content: {prompt['content']}")
                    print(f"Topics: {', '.join(prompt['topics'])}")

        elif choice == "3":
            # Search prompts
            if not prompts:
                print("No prompts found.")
            else:
                search_term = input("Enter search term: ").lower()
                found_prompts = []

                # Search through all prompts
                for prompt in prompts:
                    # Check if search term exists in title, content, or topics
                    if (search_term in prompt['title'].lower() or
                        search_term in prompt['content'].lower() or
                            any(search_term in topic.lower() for topic in prompt['topics'])):
                        found_prompts.append(prompt)

                # Display results
                if found_prompts:
                    print(f"\nFound {len(found_prompts)} matching prompts:")
                    for index, prompt in enumerate(found_prompts):
                        print(f"\nPrompt #{index + 1}:")
                        print(f"Title: {prompt['title']}")
                        print(f"Content: {prompt['content']}")
                        print(f"Topics: {', '.join(prompt['topics'])}")
                else:
                    print("No matching prompts found.")

        elif choice == "4":
            # Exit the program
            print("Thank you for using Simple Prompt Manager!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


# This conditional ensures the main() function runs only when the script is executed directly
if __name__ == "__main__":
    main()
