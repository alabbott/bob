-- Create the Users table
CREATE TABLE Users (
    ID serial PRIMARY KEY,
    Name varchar(255) NOT NULL,
    PhoneNumber varchar(255) NOT NULL
);

-- Create the Food table
CREATE TABLE Food (
    ID serial PRIMARY KEY,
    Item varchar(255) NOT NULL,
    UID int REFERENCES Users(ID) NOT NULL,
    Calories int NOT NULL,
    DateTime timestamp NOT NULL
);

-- Create the Weight table
CREATE TABLE Weight (
    ID serial PRIMARY KEY,
    Weight int NOT NULL,
    UID int REFERENCES Users(ID) NOT NULL,
    DateTime timestamp NOT NULL
);

-- Create the WeightGoals table
CREATE TABLE WeightGoals (
    ID serial PRIMARY KEY,
    UID int REFERENCES Users(ID) NOT NULL,
    GoalWeight int NOT NULL,
    StartingWeight int NOT NULL,
    DateTime timestamp NOT NULL
);

-- Create the CalorieGoals table
CREATE TABLE CalorieGoals (
    ID serial PRIMARY KEY,
    UID int REFERENCES Users(ID) NOT NULL,
    TargetCalories int NOT NULL,
    DateTime timestamp NOT NULL
);

-- Create the ActivityGoals table
CREATE TABLE ActivityGoals (
    ID serial PRIMARY KEY,
    UID int REFERENCES Users(ID) NOT NULL,
    TargetActivity int NOT NULL,
    DateTime timestamp NOT NULL
);