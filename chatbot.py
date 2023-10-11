import openai

# Replace with your OpenAI API key
api_key = "sk-qpdvzMLJ8lK6QiXj9yUUJ2A0yuZ6NKHuqaEJL1OqFGG5EvyW"

# Initialize the OpenAI API client
openai.api_key = api_key

# Function to create Helm charts based on user input
def create_helm_charts_bot():
    # Ask the initial question
    user_input = input("Do you want to create Helm charts for any open source application or is this your own application? ")

    if user_input.lower() == "open source":
        # If user wants Helm charts for an open source application
        app_name = input("Great! Please specify the name of the open source application: ")
        # You can search for Helm charts online and provide links here
        search_results = f"Here are some Helm charts for {app_name}:\n1. Link1\n2. Link2"
        print(search_results)
    elif user_input.lower() == "my own application":
        # If it's the user's own application, ask for application details
        app_name = input("What is the name of your application? ")
        deployment_type = input("Is this a Deployment or StatefulSet? ")
        need_ingress = input("Do you need Ingress for your application? (yes/no) ")
        
        # Generate Helm chart based on user's input
        prompt = f"Create Helm chart for {app_name} with {deployment_type} and Ingress: {need_ingress}"
        response = openai.Completion.create(
            engine="davinci",
            prompt=prompt,
            max_tokens=100
        )

        # Display the generated Helm chart
        print("Here is your Helm chart:")
        print(response.choices[0].text)
    else:
        print("Invalid input. Please specify 'open source' or 'my own application'.")

if __name__ == "__main__":
    create_helm_charts_bot()