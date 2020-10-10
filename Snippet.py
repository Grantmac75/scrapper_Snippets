n = 1
# Variable of div location for day of the month
i = 1
# 4 months of data
while n <= 4:

    # Identify number of days in the month that have a workout - store in NumDays
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    time.sleep(1)
    numDays = soup.find_all("div", {"class": "day same-month full"})
    # numDays = numDays + soup.find_all("div", {"class": "day same-month empty"})
    numDays = len(numDays)
    num = 1
    time.sleep(1)

    while num <= numDays:
            try:
                # selects the first day of the month using the div position from a variable and clicks the button
                dayButton = driver.find_element_by_xpath(
                    '//*[@id="app"]/div[1]/div/div/div[2]/div/div[3]/div/div['
                    + str(i)
                    + "]/div[2]"
                )
                dayButton.click()
                time.sleep(3)

                # retrieve the source code with the sidebar and creating a Soup
                htmlday = driver.page_source
                soupday = BeautifulSoup(htmlday, "html.parser")
                time.sleep(1)
                # Extract the date of the workout
                dayDate = soupday.find("div", {"class": "position"}).text
                # Finding the number of workouts for that day
                workouts = soupday.find_all("div", {"class": "section-field__body"})

                # Extracting each of the workouts for the day
                for workout in workouts:
                    # Retrieving the program name
                    program = workout.find("h4").text.strip()
                    # Retrieving the training session
                    session = workout.find("div", {"class": "description"})

                    new_row = {"Date": dayDate, "Program": program, "Session": session}

                    dailyProgram_df = dailyProgram_df.append(new_row, ignore_index=True)

                i = i + 1

                # Close sidetabe
                closeButton()
                time.sleep(2)

            except:
                i = i + 1

            num = num + 1
        else:
            num = num + 1
            numDays = numDays + 1


    n = n + 1

    # Move to next month
    forwardButton()
    time.sleep(3)