import traceback
if __name__ == "__main__"
try:
    from email.mime.text import MIMEText
    import requests
    import random
    import yagmail
    from datetime import datetime, timedelta

    def weather_call():

        # Get tomorrow's date
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%Y-%m-%d")

        # Build the API URL
        url = (
            f"https://api.open-meteo.com/v1/forecast?"
            f"latitude=-43.53&longitude=172.63"
            f"&hourly=temperature_2m,precipitation"
            f"&timezone=auto"
            f"&start_date={tomorrow}&end_date={tomorrow}"
        )

        # Fetch data
        response = requests.get(url)
        try:
            data = response.json()
            times = data["hourly"]["time"]
            temps = data["hourly"]["temperature_2m"]
            precip = data["hourly"]["precipitation"]
        except ValueError:
            print("weather API did not return valid JSON.")
            return("No Weather today 😞")
        

        # Target hour (e.g., 09:00)
        target_hour = f"{tomorrow}T12:00"

        # Find the index of that hour
        if target_hour in times:
            idx = times.index(target_hour)
            print(f"Forecast for {target_hour}: {temps[idx]}°C, {precip[idx]}mm rain")
            return(f"Forecast for {datetime.now().strftime('%B %d, %Y')}: {temps[idx]}°C, {precip[idx]}mm rain, at 12:00")
        else:
            print("Target hour not available.")


    def joke_call():
        url = "https://v2.jokeapi.dev/joke/Any?blacklistFlags=nsfw,religious,racist,explicit"
        response = requests.get(url)
        try:
            data = response.json()
        except ValueError:
            print("Joke API did not return valid JSON.")
            return ("No joke today 😞")
            

        if data["type"] == "single":
            print(data["joke"])
            part_one=data["joke"]
            part_two=""
            return(part_one)
        elif data["type"] == "twopart":
            print(data["setup"])
            print(data["delivery"])
            part_one=data["setup"]
            part_two=data["delivery"]
            return(f"Q : {part_one} : A : {part_two}")
        else:
            print("Unexpected joke format")
        
    def advice_call():
        url = "https://api.adviceslip.com/advice"
        response = requests.get(url)
        try:
            data = response.json()
        except ValueError:
            print("advice API did not return valid JSON.")
            return "No Advice today 😞"
        advice = data["slip"]["advice"]
        print(advice)
        return(advice)
    


    def definition_call(word):
            try:
                url=f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"
                response = requests.get(url)
                data=response.json()
                definition = data[0]['meanings'][0]['definitions'][0]['definition']
                return(definition)
            except:
                print("nah")
                return("N/A")

    def word_call():
            url = "https://api.datamuse.com/words?sp=????"
            response = requests.get(url)

            try:
                words = response.json()
                word = random.choice(words)["word"]
                definition = definition_call(word)
                print(definition)
                return(f"{word} - {definition}")
            except:
                return("Could not fetch word.")
            
    def news_call():
        current_date = datetime.today().strftime("%Y-%m-%d")
        date_obj = datetime.strptime(current_date, "%Y-%m-%d")  # convert string to datetime
        new_date = date_obj - timedelta(days=2) 
        url=f"https://newsapi.org/v2/everything?q=New%20Zealand&from={new_date}&to={current_date}&sortBy=publishedAt&apiKey=903c54ba7d6446c3bdb66c74725354b6"
        response=requests.get(url)
        try:
            data=response.json()
            print(data)
            print()
            total_news_report = []

            for item in data["articles"]:
                current_news_report = {
                    "title": item["title"],
                    "description": item["description"],
                    "url": item["url"]
                }
                total_news_report.append(current_news_report)

            # Pick a random article
            index = random.randint(0, len(total_news_report) - 1)
            selected = total_news_report[index]

            title = selected["title"]
            description = selected["description"]
            url = selected["url"]
            return(f"""<td style="padding": 10px 0;"><strong>📰 Some head lines today:</strong><br><a href="{url} target="_blank"">{title}<a><br>{description}</td>""")
        except:
            return("Cannot find any news today")
            
    yag = yagmail.SMTP('dailly.internet.blast@gmail.com', 'eurkvzcyfdavtjer')
    weather=weather_call()
    advice=advice_call()
    joke=joke_call()
    word=word_call()
    news=news_call()

    people_who_have_subcribed=[
        ["Ethan","ethan.connor.lord06@gmail.com"]#,
        #["Mum","dionne.lord77@gmail.com"],
        #["Rylan","charmanderlocksofgatesandkeys@gmail.com"],
        #["Cohen","owner@ocebedwars.com"],
        #["Joseph","joe.jenkinson5@gmail.com"],
        #["Hunter Lovell","hunter.lovell2009@gmail.com"],
        #["Dad","brian.lord.meadowbrook@gmail.com"]
    ]
    for items in people_who_have_subcribed:
        message = f"""
            <html>
            <body style="margin: 0; padding: 0; background: #ececec;">
                <table role="presentation" width="100%" cellpadding="0" cellspacing="0" style="font-family: 'Segoe UI', sans-serif;">
                    <tr>
                        <td align="center" style="padding: 40px 20px;">
                            <table width="600" cellpadding="0" cellspacing="0" style="background: #ffffff; border-radius: 10px; overflow: hidden; box-shadow: 0 5px 20px rgba(0,0,0,0.1);">
                                <tr>
                                    <td style="background: linear-gradient(90deg, #6dd5fa, #2980b9); color: white; padding: 30px; text-align: center;">
                                        <h1 style="margin: 0; font-size: 28px;">🌞 Good Morning, {items[0]}!</h1>
                                        <p style="margin: 10px 0 0; font-size: 16px;">Here’s your daily refresh 🌿</p>
                                    </td>
                                </tr>
                                <tr>
                                    <td align="center" style="padding: 40px 20px;">
                                        <table width="100%" cellpadding="0" cellspacing="0" style="font-size: 16px; color: #333333; background: #FFF9C4;">
                                            <tr>
                                                <td style="padding: 10px 0;"><strong>🌤️ Weather:</strong><br>{weather}</td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 10px 0;"><strong>💡 Quote:</strong><br>{advice}</td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 10px 0;"><strong>😂 Joke:</strong><br>{joke}</td>
                                            </tr>
                                            <tr>
                                                <td style="padding: 10px 0;"><strong>✍️ Word of the Day:</strong><br>{word}</td>
                                            </tr>
                                            <tr>
                                                {news}
                                            </tr>
                                        </table>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="background: #f5f5f5; padding: 20px; text-align: center; font-size: 14px; color: #777;">
                                        🌈 Make today amazing!<br>
                                        <em>This message was auto-generated by your Daily Internet Blast.</em>
                                    </td>
                                </tr>
                            </table>
                        </td>
                    </tr>
                </table>
            </body>
            </html>
            """


        print(message)


            # Send an email
        yag.send(items[1],f"Your Daily Digest – {datetime.now().strftime('%B %d, %Y')}",message )
        print(f"{items[0]}'s one sent")

    with open("C:\\Users\\ethan\\OneDrive\\Desktop\\error_log.txt", "w") as f:
        f.write("Sent correctly")



except Exception as e:
    print("Nah nice try")
    print(e)
    with open("C:\\Users\\ethan\\OneDrive\\Desktop\\error_log.txt", "w") as f:
        f.write("Error:\n")
        traceback.print_exc(file=f)
        

