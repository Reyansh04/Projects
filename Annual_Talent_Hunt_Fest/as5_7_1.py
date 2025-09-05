import math
import csv

def age(year, month, day):
    days_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
                 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_dict[2] = 29
    day_count = day
    for m in range(1, month):
        day_count += days_dict[m]
    if days_dict[2] == 29:
            total_days = 366
    else:
        total_days = 365
    return year + day_count / total_days


class Participant:
    def __init__(self, name, idi, birth_year, birth_month, birth_day, gender):
        self.name = str(name)
        self.idi = int(idi)
        self.__birth_year = int(birth_year)
        self.__birth_month = int(birth_month)
        self.__birth_day = int(birth_day)
        self.__gender = str(gender)

    def get_values(self):
        return (self.name, self.idi,self.__birth_year, self.__birth_month, self.__birth_day, self.__gender)

    def show_values(self):
        print(*self.get_values())

    def calculate_age(self, current_day, current_month, current_year):
        if (current_day < 1 or current_year < 0 or current_month < 1 or current_month > 12):
            return -1
        days_dict = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
        if (current_year % 4 == 0 and current_year % 100 != 0) or (current_year % 400 == 0):
            days_dict[2] = 29
        if current_day > days_dict[current_month]:
            return -1
        current_age = age(current_year, current_month, current_day)
        birth_age = age(self.__birth_year, self.__birth_month, self.__birth_day)
        return math.floor(current_age - birth_age)

    def set_values(self, data_attributes: dict):
        if "name" in data_attributes:
            self.name = str(data_attributes["name"])
        if "idi" in data_attributes:
            self.idi = int(data_attributes["idi"])
        if "birth_year" in data_attributes:
            self.__birth_year = int(data_attributes["birth_year"])
        if "birth_month" in data_attributes:
            self.__birth_month = int(data_attributes["birth_month"])
        if "birth_day" in data_attributes:
            self.__birth_day = int(data_attributes["birth_day"])
        if "gender" in data_attributes:
            self.__gender = str(data_attributes["gender"])

class Student(Participant):
    def __init__(self, name, idi, birth_year, birth_month, birth_day, gender,
                 grade_level, class_assigned, gpa,
                 selected_activity, talent_score, athletic_score, leadership_score):
        super().__init__(name, idi, birth_year, birth_month, birth_day, gender)
        self.__age = super().calculate_age(1, 1, 2025)
        self.__grade_level = int(grade_level)
        self.__class_assigned = str(class_assigned)
        gpa_val = float(gpa)
        if not (0.0 <= gpa_val <= 10.0):
            return -1
        self.__gpa = gpa_val
        self.__selected_activity = str(selected_activity)
        self.__talent_score = float(talent_score)
        self.__athletic_score = float(athletic_score)
        self.__leadership_score = float(leadership_score)
        self.__eligible = (gpa_val >= 5.0)

    def is_eligible(self):
        if self.__gpa >= 5.0:
            self.__eligible = True
        else:
            self.__eligible = False
        return self.__eligible

    def get_values(self):
        return (self.name, self.idi, self._Participant__birth_year, self._Participant__birth_month,
                self._Participant__birth_day, self._Participant__gender,self.__age, self.__grade_level,
                self.__class_assigned, self.__gpa, self.__selected_activity,self.__talent_score, 
                self.__athletic_score, self.__leadership_score, self.__eligible)

    def show_values(self):
        print(*self.get_values())

    def set_values(self, data_attributes: dict):
        super().set_values(data_attributes)
        if "grade_level" in data_attributes:
            self.__grade_level = int(data_attributes["grade_level"])
        if "class_assigned" in data_attributes:
            self.__class_assigned = str(data_attributes["class_assigned"])
        if "gpa" in data_attributes:
            gpa_val = float(data_attributes["gpa"])
            if not (0.0 <= gpa_val <= 10.0):
                raise ValueError("INVALID INPUT: GPA must be between 0 and 10")
            self.__gpa = gpa_val
            self.is_eligible()
        if "selected_activity" in data_attributes:
            self.__selected_activity = str(data_attributes["selected_activity"])
        if "talent_score" in data_attributes:
            self.__talent_score = float(data_attributes["talent_score"])
        if "athletic_score" in data_attributes:
            self.__athletic_score = float(data_attributes["athletic_score"])
        if "leadership_score" in data_attributes:
            self.__leadership_score = float(data_attributes["leadership_score"])
        if any(k in data_attributes for k in ("birth_year", "birth_month", "birth_day")):
            self.__age = super().calculate_age(1, 1, 2025)

class Teacher(Participant):
    def __init__(self, name, idi, birth_year, birth_month, birth_day, gender,
                 subject, mentor_grade, mentor_class, judge):
        super().__init__(name, idi, birth_year, birth_month, birth_day, gender)
        self.__subject = str(subject)
        self.__mentor_grade = int(mentor_grade)
        self.__mentor_class = str(mentor_class)
        self.__judge = bool(judge)

    def get_values(self):
        return (self.name, self.idi, self._Participant__birth_year, self._Participant__birth_month,
                self._Participant__birth_day, self._Participant__gender,self.__subject, self.__mentor_grade,
                self.__mentor_class, self.__judge)

    def show_values(self):
        print(*self.get_values())

    def set_values(self, data_attributes: dict):
        super().set_values(data_attributes)
        if "subject" in data_attributes:
            self.__subject = str(data_attributes["subject"])
        if "mentor_grade" in data_attributes:
            self.__mentor_grade = int(data_attributes["mentor_grade"])
        if "mentor_class" in data_attributes:
            self.__mentor_class = str(data_attributes["mentor_class"])
        if "judge" in data_attributes:
            self.__judge = bool(data_attributes["judge"])

class Artist(Student):
    def __init__(self, name, idi, birth_year, birth_month, birth_day, gender, 
                 grade_level, class_assigned, gpa,
                 selected_activity, talent_score, athletic_score, leadership_score, talent):
        super().__init__(name, idi, birth_year, birth_month, birth_day, gender, 
                        grade_level, class_assigned, gpa, selected_activity, talent_score,
                        athletic_score, leadership_score)
        self.__performance_level = self._Student__talent_score
        self.__talent = talent
    
    def is_eligible(self):
        if (self._Student__age >= 16) and (self._Student__gpa > 6):
            eligibility_data = {"eligible": True}
            super().set_values(eligibility_data)
            return True
        else:
            return False
    
    def get_values(self):
        student_values = super().get_values()
        artist_values = (self.__talent, self.__performance_level)
        return student_values + artist_values
    
    def compute_scores(self):
        if self.is_eligible():
            return self.__performance_level
        else:
            return -1
    
    def show_values(self):
        print(*self.get_values())
    
    def set_values(self, data_attributes: dict):
        super().set_values(data_attributes)
        if "talent" in data_attributes:
            self.__talent = data_attributes["talent"]
        if "performance_level" in data_attributes:
            self.__performance_level = data_attributes["performance_level"]
        self.__performance_level = self._Student__talent_score

class Athlete(Student):
    def __init__(self, name, idi, birth_year, birth_month, birth_day, gender, 
                 grade_level, class_assigned, gpa,
                 selected_activity, talent_score, athletic_score, leadership_score, sports_category,
                 fitness_score):
        super().__init__(name, idi, birth_year, birth_month, birth_day, gender, 
                        grade_level, class_assigned, gpa, selected_activity, talent_score,
                        athletic_score, leadership_score)
        self.__sports_category = sports_category
        self.__fitness_score = fitness_score
        self.__performance_level = self._Student__athletic_score
    
    def is_eligible(self):
        if (self._Student__age >= 12) and (self._Student__gpa > 5.5):
            eligibility_data = {"eligible": True}
            super().set_values(eligibility_data)
            return True
        else:
            return False
    
    def compute_scores(self):
        if self.is_eligible():
            return self.__fitness_score*self.__performance_level
        else:
            return -1
    
    def get_values(self):
        student_values = super().get_values()
        athlete_values = (self.__sports_category, self.__fitness_score, self.__performance_level)
        return student_values + athlete_values
    
    def show_values(self):
        print(*self.get_values())
    
    def set_values(self, data_attributes):
        super().set_values(data_attributes)
        if "sports_category" in data_attributes:
            self.__sports_category = data_attributes["sports_category"]
        if "fitness_score" in data_attributes:
            self.__fitness_score = data_attributes["fitness_score"]
        if "performance_level" in data_attributes:
            self.__performance_level = data_attributes["performance_level"]
            if data_attributes["performance_level"] != self._Student__athletic_score:
                return -1
        self.__performance_level = self._Student__athletic_score

class Scholar(Student):
    def __init__(self, name, idi, birth_year, birth_month, birth_day, gender, 
                 grade_level, class_assigned, gpa,
                 selected_activity, talent_score, athletic_score, leadership_score, subject_specialization,
                 olympiad_scores):
        super().__init__(name, idi, birth_year, birth_month, birth_day, gender, 
                        grade_level, class_assigned, gpa, selected_activity, talent_score, 
                        athletic_score, leadership_score)
        self.__subject_specialization = subject_specialization
        self.__olympiad_scores = olympiad_scores
        self.__performance_level = self._Student__gpa * 10

    def is_eligible(self):
        if ((self._Student__age >= 10) and (self._Student__gpa > 8.0) and 
            any(i > 80 for i in self.__olympiad_scores)):
            eligibility_data = {"eligible": True}
            super().set_values(eligibility_data)
            return True
        else:
            return False
    
    def get_values(self):
        student_values = super().get_values()
        scholar_values = (self.__subject_specialization, self.__olympiad_scores, self.__performance_level)
        return student_values + scholar_values
    
    def show_values(self):
        print(*self.get_values())
    
    def compute_scores(self):
        if self.is_eligible():
            return sum(score * self.__performance_level for score in self.__olympiad_scores)
        else:
            return -1
    
    def set_values(self, data_attributes):
        super().set_values(data_attributes)
        if "subject_specialization" in data_attributes: 
            self.__subject_specialization = data_attributes["subject_specialization"]
        if "olympiad_scores" in data_attributes:
            self.__olympiad_scores = data_attributes["olympiad_scores"]
        if "performance_level" in data_attributes:
            if data_attributes['performance_level'] != self._Student__gpa*10:
                return -1
            self.__performance_level = data_attributes["performance_level"]
        self.__performance_level = self._Student__gpa*10

class Activity:
    def __init__(self, activity_id, activity_name, activity_type, max_participants,
                 grade_level, is_active, participants, organizers):
        self.activity_id = int(activity_id)
        self.activity_name = str(activity_name)
        self.__activity_type = str(activity_type)
        self.__max_participants = int(max_participants)
        self.__grade_level = int(grade_level)
        self.__is_active = bool(is_active)
        self.__participants = list(participants)
        self.__organizers = list(organizers)
    
    def get_values(self):
        participant_name = list([p.name for p in self.__participants])
        paricipant_organizers = list([q.name for q in self.__organizers])
        return (self.activity_id, self.activity_name, self.__activity_type, self.__max_participants, 
                self.__grade_level, self.__is_active, participant_name, paricipant_organizers)

    def set_values(self, data_attributes):
        if "activity_type" in data_attributes:
            self.__activity_type= data_attributes["activity_type"]
        if "max_participants" in data_attributes:
            self.__max_participants = data_attributes["max_participants"]
        if "grade_level" in data_attributes:
            self.__grade_level = data_attributes["grade_level"]
        if "is_active" in data_attributes:
            self.__is_active = data_attributes["is_active"]
        if "participants" in data_attributes:
            self.__participants = data_attributes["participants"]
        if "organizers" in data_attributes:
            self.__organizers = data_attributes["organizers"]

    def show_values(self):
        print(*self.get_values())

class SportsTournament(Activity):
    def __init__(self, activity_id, activity_name, activity_type, max_participants,
                 grade_level, is_active, participants, organizers, game_type, duration_minutes):
        super().__init__(activity_id, activity_name, activity_type, max_participants,
                 grade_level, is_active, participants, organizers)
        if game_type not in ("Team", "Individual"):
            return -1
        self.__game_type = str(game_type)
        self.__duration_minutes = int(duration_minutes)
        for i in self._Activity__participants:
            if type(i) != Athlete:
                return -1
    def get_values(self):
        activity_values = super().get_values()
        sport_values = (self.__game_type, self.__duration_minutes)
        return activity_values + sport_values
    
    def show_values(self):
        print(*self.get_values())
    
    def determine_winner(self):       
        if self.__game_type == "Individual":
            a = self._Activity__participants[0]
            b = self._Activity__participants[0].compute_scores()
            for i in self._Activity__participants:
                if b < i.compute_scores():
                    a = i
                    b = i.compute_scores()
            return a
        
        elif self.__game_type == "Team":
            a = {}
            for i in self._Activity__participants:
                key = i._Student__class_assigned
                if key not in a:
                    a[key] = [i]
                else:
                    a[key].append(i)
            teams = list(a.values())
            teamscore = []
            for i in range(len(teams)):
                score = 0
                team_len = len(teams[i])
                for j in teams[i]:
                    score += j.compute_scores()
                avg_score = score / team_len
                teamscore.append(avg_score)
            win_team = teams[teamscore.index(max(teamscore))]
            ab = win_team[0]
            b = ab.compute_scores()
            for i in win_team:
                if b < i.compute_scores():
                    ab = i
                    b = i.compute_scores()
            return ab

class TalentShow(Activity):
    def __init__(self, activity_id, activity_name, activity_type, max_participants,
                 grade_level, is_active, participants, organizers, talent_categories):
        super().__init__(activity_id, activity_name, activity_type, max_participants, 
                         grade_level, is_active, participants, organizers)
        self.__talent_categories = talent_categories
        for i in self._Activity__participants:
            if type(i) != Artist:
                return -1
    
    def evaluate_talent(self):
        a = self._Activity__participants[0]._Artist__performance_level
        b = self._Activity__participants[0]
        for i in self._Activity__participants:
            if i._Artist__performance_level > a:
                a = i._Artist__performance_level
                b = i
        return b
    
    def get_values(self):
        activity_values = super().get_values()
        talent_values = (self.__talent_categories,)
        return activity_values + talent_values
    
    def show_values(self):
        print(*self.get_values())
    
    def determine_winner(self):
        if not self._Activity__participants:
            return -1
        best_participant = None
        highest_score = -1
        for participant in self._Activity__participants:       
            score = participant.compute_scores()
            if score > highest_score:
                highest_score = score
                best_participant = participant
        if best_participant:
            return best_participant  
        else:
            return -1

class AcademicCompetition(Activity):
    def __init__(self, activity_id, activity_name, activity_type, max_participants,
                 grade_level, is_active, participants, organizers, subjects, max_marks):
        super().__init__(activity_id, activity_name, activity_type, max_participants, 
                         grade_level, is_active, participants, organizers)
        list1 = []
        a = str(subjects)
        list1.append(a)
        self.__subjects = list1
        self.__max_marks = float(max_marks)
        for i in self._Activity__participants:
            if type(i) != Scholar:
                return -1
    
    def determine_winner(self):
        if not self._Activity__participants:
            return -1
        best_participant = None
        highest_score = -1
        for participant in self._Activity__participants:       
            score = participant.compute_scores()
            if score > highest_score:
                highest_score = score
                best_participant = participant
        if best_participant:
            return best_participant  
        else:
            return -1

    def get_values(self):
        activity_values = super().get_values()
        acad_values = (self.__subjects, self.__max_marks)
        return activity_values + acad_values
    
    def show_values(self):
        print(*self.get_values()) 


def load_participant_data(filepath):
    student_list = []
    teacher_list = []
    with open(filepath, mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Check if it's a teacher (they have subject)
            if row['subject'] != "" and row['gpa'] == "":
                '''
                if (row['mentor_grade'] == "" or row['mentor_class'] == "" or row['judge'] == "" or 
                row['idi'] == "" or row['name'] == "" or row['birth_year'] == "" or row['birth_month'] == ""
                or row['birth_day'] == "" or row["gender"] == "" or row["subject"] == ""):
                    print("INVALID INPUT 01")
                    return -1
                '''
                teacher = Teacher(
                    name=row['name'], 
                    idi=int(row['idi']),
                    birth_year=int(row['birth_year']), 
                    birth_month=int(row['birth_month']), 
                    birth_day=int(row['birth_day']),
                    gender=row['gender'],
                    subject=row['subject'],
                    mentor_grade=int(row['mentor_grade']),
                    mentor_class=row['mentor_class'],
                    judge=bool(row["judge"] == "True")  # Convert string to boolean
                    )
                teacher_list.append(teacher)
                # Check if it's a student (they have GPA)
            elif row['gpa'] != "" and row['subject'] == "":
                    # Check for Scholar (has subject_specialization and olympiad_scores)
                if row['subject_specialization'] != "" and row['olympiad_scores'] != "":
                    '''
                    if (row["name"] == "" or row["idi"] == "" or row["birth_year"] == "" or row["birth_month"] == "" 
                    or row["birth_day"] == "" or row["gender"] == "" or row["grade_level"] == "" 
                    or row["class_assigned"] == "" or row["gpa"] == "" or row["selected_activity"] == "" 
                    or row["talent_score"] == "" or row["athletic_score"] == "" or row["leadership_score"] == ""):
                        print("INVALID INPUT 02")
                        exit()
                    '''
                    if "-" in row["olympiad_scores"]:
                        scores = [int(i) for i in row['olympiad_scores'].split("-")]
                    else:
                        scores = row["olympiad_scores"]
                    student = Scholar(
                                name=row['name'],
                                idi=int(row['idi']),
                                birth_year=int(row['birth_year']),
                                birth_month=int(row['birth_month']),
                                birth_day=int(row['birth_day']),
                                gender=row['gender'],
                                grade_level=int(row['grade_level']),
                                class_assigned=row['class_assigned'],
                                gpa=float(row['gpa']),
                                selected_activity=row['selected_activity'],
                                talent_score=float(row['talent_score']),
                                athletic_score=float(row['athletic_score']),
                                leadership_score=float(row['leadership_score']),
                                subject_specialization=row['subject_specialization'],
                                olympiad_scores=scores
                                )
                    student_list.append(student)
                    # Check for Athlete (has sports_category and fitness_score)
                elif row['sports_category'] != "" and row['fitness_score'] != "":
                    '''
                    if (row["name"] == "" or row["idi"] == "" or row["birth_year"] == "" or row["birth_month"] == ""
                    or row["birth_day"] == "" or row["gender"] == "" or row["grade_level"] == ""
                    or row["class_assigned"] == "" or row["gpa"] == "" or row["selected_activity"] == "" or 
                    row["talent_score"] == "" or row["athletic_score"] == "" or row["leadership_score"] == "" 
                    or row["sports_category"] == "" or row["fitness_score"] == ""):
                        print("INVALID INPUT 03")
                        return -1
                    '''
                    student = Athlete(
                            name=row['name'], 
                            idi=int(row['idi']),
                            birth_year=int(row['birth_year']), 
                            birth_month=int(row['birth_month']), 
                            birth_day=int(row['birth_day']),
                            gender=row['gender'],
                            grade_level=int(row['grade_level']), 
                            class_assigned=row['class_assigned'],
                            gpa=float(row['gpa']),
                            selected_activity=row['selected_activity'],
                            talent_score=float(row['talent_score']), 
                            athletic_score=float(row['athletic_score']), 
                            leadership_score=float(row['leadership_score']),
                            sports_category=row['sports_category'],
                            fitness_score=float(row['fitness_score'])
                            )
                    student_list.append(student)
                        # Check for Artist (has talent)
                elif row['talent'] != "":
                    '''
                    if (row["name"] == "" or row["idi"] == "" or row["birth_year"] == "" or row["birth_month"] == ""
                    or row["birth_day"] == "" or row["gender"] or row["grade_level"] == "" or row["class_assigned"] == ""
                    or row["gpa"] == "" or row["selected_activity"] == "" or row["talent_score"] == "" or row["athletic_score"] == ""
                    or row["leadership_score"] == "" or row["talent"] == ""):
                        print("INVALID INPUT 04")
                        return -1
                    ''' 
                    student = Artist(
                            name=row['name'], 
                            idi=int(row['idi']),
                            birth_year=int(row['birth_year']), 
                            birth_month=int(row['birth_month']), 
                            birth_day=int(row['birth_day']),
                            gender=row['gender'],
                            grade_level=int(row['grade_level']), 
                            class_assigned=row['class_assigned'],
                            gpa=float(row['gpa']),
                            selected_activity=row['selected_activity'],
                            talent_score=float(row['talent_score']), 
                            athletic_score=float(row['athletic_score']), 
                            leadership_score=float(row['leadership_score']),
                            talent=row['talent']
                            )
                    student_list.append(student)
                # Create a basic Student if no specialized type
                elif row["gpa"] != "":
                    '''
                    if (row["name"] == "" or row["idi"] == "" or row["birth_year"] == "" or row["birth_month"] == ""
                    or row["birth_day"] == "" or row["gender"] == "" or row["grade_level"] == "" or row["class_assigned"] == ""
                    or row["gpa"] == "" or row["selected_activity"] == "" or row["talent_score"] == "" or row["athletic_score"] == ""
                    or row["leadership_score"] == ""):
                        print("INVALID INPUT 05")
                        return -1
                    '''
                    student = Student(
                                name=row['name'], 
                                idi=int(row['idi']),
                                birth_year=int(row['birth_year']), 
                                birth_month=int(row['birth_month']), 
                                birth_day=int(row['birth_day']),
                                gender=row['gender'],
                                grade_level=int(row['grade_level']), 
                                class_assigned=row['class_assigned'],
                                gpa=float(row['gpa']),
                                selected_activity=row['selected_activity'],
                                talent_score=float(row['talent_score']), 
                                athletic_score=float(row['athletic_score']), 
                                leadership_score=float(row['leadership_score'])
                            )
                    student_list.append(student)
                else:
                    print("INVALID INPUT 06")
                    return -1           
    return (student_list, teacher_list)

def load_activities_data(filepath):
    sports_tournament_list = []
    talent_show_list = []
    academic_competition_list = []
    with open(filepath, mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            # Check if it's a sports tournament
            if row['activity_type'] == "Sports":
                
                if (row["activity_id"] == "" or row["activity_name"] == "" or row["activity_type"] == ""
                    or row["max_participants"] == "" or row["grade_level"] == "" or row["game_type"] == ""
                    or row["duration_minutes"] == "" ):
                    print("INVALID INPUT")
                    return -1
                
                activity = SportsTournament(
                    activity_id=int(row['activity_id']),
                    activity_name=str(row['activity_name']),
                    activity_type=str(row['activity_type']),
                    max_participants=int(row['max_participants']),
                    grade_level=int(row['grade_level']),
                    is_active=False,
                    participants=[],
                    organizers=[],
                    game_type=str(row['game_type']),
                    duration_minutes=int(row['duration_minutes'])
                )
                sports_tournament_list.append(activity)
            #check if it is a Talent SHow
            elif row['activity_type'] == "Talent":
                
                if (row['activity_id'] == "" or row['activity_name'] == "" or
                    row['activity_type'] == "" or row['max_participants'] == "" or
                    row['grade_level'] == "" or row['talent_categories'] == ""):
                    print("INVALID INPUT")
                    exit()
                #talent_categories = row['talent_categories'].split("-")
                if "-" in row["talent_categories"]:
                    abc = [i for i in row['talent_categories'].split("-")]
                else:
                    abc = [row['talent_categories']]
                activity = TalentShow(
                    activity_id=int(row['activity_id']),
                    activity_name=str(row['activity_name']),
                    activity_type=str(row['activity_type']),
                    max_participants=int(row['max_participants']),
                    grade_level=int(row['grade_level']),
                    is_active=False,
                    participants=[],
                    organizers=[],
                    talent_categories = abc
                )
                talent_show_list.append(activity)
            #check if it is an Academic Competition
            elif row['activity_type'] == "Academic":
                
                if (row['activity_id'] == "" or row['activity_name'] == "" or row['activity_type'] == "" or
                    row['max_participants'] == "" or row['grade_level'] == "" or row['subjects'] == "" or 
                    row["max_marks"] == ""):
                    print("INVALID INPUT")
                    return -1
                
                activity = AcademicCompetition(
                    activity_id=int(row['activity_id']),
                    activity_name=str(row['activity_name']),
                    activity_type=str(row['activity_type']),
                    max_participants=int(row['max_participants']),
                    grade_level=int(row['grade_level']),
                    is_active=False,
                    participants=[],
                    organizers=[],
                    subjects=row['subjects'],
                    max_marks=float(row['max_marks'])
                )
                academic_competition_list.append(activity)
            else:
                print("INVALID INPUT")
                return -1
    return (sports_tournament_list, talent_show_list, academic_competition_list)

def specialised_students(filepath):
    artist_list = []
    athlete_list = []
    scholar_list = []
    
    with open(filepath, mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            if row["selected_activity"] == "Sports":
                student = Athlete(
                    name=row['name'],
                    idi=int(row['idi']),
                    birth_year=int(row['birth_year']),
                    birth_month=int(row['birth_month']),
                    birth_day=int(row['birth_day']),
                    gender=row['gender'],
                    grade_level=int(row['grade_level']),
                    class_assigned=row['class_assigned'],
                    gpa=float(row['gpa']),
                    selected_activity=row['selected_activity'],
                    talent_score=float(row['talent_score']),
                    athletic_score=float(row['athletic_score']),
                    leadership_score=float(row['leadership_score']),
                    sports_category=row['sports_category'],
                    fitness_score=float(row['fitness_score'])
                )
                athlete_list.append(student)
            elif row["selected_activity"] == "Talent":
                student = Artist(
                    name=row['name'],
                    idi=int(row['idi']),
                    birth_year=int(row['birth_year']),
                    birth_month=int(row['birth_month']),
                    birth_day=int(row['birth_day']),
                    gender=row['gender'],
                    grade_level=int(row['grade_level']),
                    class_assigned=row['class_assigned'],
                    gpa=float(row['gpa']),
                    selected_activity=row['selected_activity'],
                    talent_score=float(row['talent_score']),
                    athletic_score=float(row['athletic_score']),
                    leadership_score=float(row['leadership_score']),
                    talent=row['talent']
                )
                artist_list.append(student)
            elif row["selected_activity"] == "Academic":
                if "-" in row["olympiad_scores"]:
                    scores = [int(i) for i in row['olympiad_scores'].split("-")]
                else:
                    scores = [int(row["olympiad_scores"])]
                student = Scholar(
                    name=row['name'],
                    idi=int(row['idi']),
                    birth_year=int(row['birth_year']),
                    birth_month=int(row['birth_month']),
                    birth_day=int(row['birth_day']),
                    gender=row['gender'],
                    grade_level=int(row['grade_level']),
                    class_assigned=row['class_assigned'],
                    gpa=float(row['gpa']),
                    selected_activity=row['selected_activity'],
                    talent_score=float(row['talent_score']),
                    athletic_score=float(row['athletic_score']),
                    leadership_score=float(row['leadership_score']),
                    subject_specialization=row['subject_specialization'],
                    olympiad_scores=scores
                )
                scholar_list.append(student)
    
    # Group by class_assigned instead of by name
    class_artists = {}
    class_scholars = {}
    class_athletes = {}
    
    for artist in artist_list:
        class_assigned = artist._Student__class_assigned
        if class_assigned in class_artists:
            class_artists[class_assigned].append(artist)
        else:
            class_artists[class_assigned] = [artist]
            
    for scholar in scholar_list:
        class_assigned = scholar._Student__class_assigned
        if class_assigned in class_scholars:
            class_scholars[class_assigned].append(scholar)
        else:
            class_scholars[class_assigned] = [scholar]
            
    for athlete in athlete_list:
        class_assigned = athlete._Student__class_assigned
        if class_assigned in class_athletes:
            class_athletes[class_assigned].append(athlete)
        else:
            class_athletes[class_assigned] = [athlete]
    
    # Use the exact field names as specified in the problem
    field_names = ["participant_id", "name", "grade_level", "class_assigned", "selected_activity", "score"]
    
    # Create CSV files with proper naming and content
    for class_assigned, artists in class_artists.items():
        with open(f"{class_assigned}-artist.csv", "w") as file:
            writer = csv.DictWriter(file, field_names)
            writer.writeheader()
            for artist in artists:
                row_dict = {
                    "participant_id": artist.idi,
                    "name": artist.name,
                    "grade_level": artist._Student__grade_level,
                    "class_assigned": artist._Student__class_assigned,
                    "selected_activity": artist._Student__selected_activity,
                    "score": artist.compute_scores()
                }
                writer.writerow(row_dict)
    
    for class_assigned, scholars in class_scholars.items():
        with open(f"{class_assigned}-scholar.csv", "w") as file:
            writer = csv.DictWriter(file, field_names)
            writer.writeheader()
            for scholar in scholars:
                row_dict = {
                    "participant_id": scholar.idi,
                    "name": scholar.name,
                    "grade_level": scholar._Student__grade_level,
                    "class_assigned": scholar._Student__class_assigned,
                    "selected_activity": scholar._Student__selected_activity,
                    "score": scholar.compute_scores()
                }
                writer.writerow(row_dict)
    
    for class_assigned, athletes in class_athletes.items():
        with open(f"{class_assigned}-athlete.csv", "w") as file:
            writer = csv.DictWriter(file, field_names)
            writer.writeheader()
            for athlete in athletes:
                row_dict = {
                    "participant_id": athlete.idi,
                    "name": athlete.name,
                    "grade_level": athlete._Student__grade_level,
                    "class_assigned": athlete._Student__class_assigned,
                    "selected_activity": athlete._Student__selected_activity,
                    "score": athlete.compute_scores()
                }
                writer.writerow(row_dict)
    
    return (artist_list, athlete_list, scholar_list)

def register_activity(participant_filepath: str, activity_filepath: str) -> tuple:
    # Load specialized student data (artists, athletes, scholars)
    spec_stud_tup = specialised_students(participant_filepath)
    if spec_stud_tup == -1:
        return -1
    
    # Load activity data
    act_stud_tup = load_activities_data(activity_filepath)
    if act_stud_tup == -1:
        return -1
    sports_tournament_list, talent_show_list, academic_competition_list = act_stud_tup
    
    # Get teacher data
    teacher_list = load_participant_data(participant_filepath)[1]
    student_activity_list = load_participant_data(participant_filepath)[0]
    artist_list, athlete_list, scholar_list = spec_stud_tup
    
    # Organize activities by type
    act_dict = {'cricket':[], "chess":[], "mathematics":[], "science":[], "computers":[], "blackrose":[]}
    
    for i in sports_tournament_list:
        activity_name = i.activity_name.lower()
        if "cricket" in activity_name:
            act_dict["cricket"].append(i)
        elif "chess" in activity_name:
            act_dict["chess"].append(i)
    
    for j in talent_show_list:
        activity_name = j.activity_name.lower()
        if "blackrose" in activity_name:
            act_dict["blackrose"].append(j)
    
    for k in academic_competition_list:
        activity_name = k.activity_name
        if "math" in activity_name:
            act_dict["mathematics"].append(k)
        elif "science" in activity_name:
            act_dict["science"].append(k)
        elif "computer" in activity_name:
            act_dict["computers"].append(k)
    
    # Create activity mapping from generic types to specific activities
    activity_mapping = {
        "sports": ["cricket", "chess"],
        "talent": ["blackrose"],
        "academic": ["mathematics", "science", "computers"]
    }
    
    # Register eligible students to appropriate activities
    '''
    for student in student_activity_list:
        if student.is_eligible():
            selected_activity = student._Student__selected_activity
            if selected_activity in activity_mapping:
                for activity_type in activity_mapping[selected_activity]:
                    for activity in act_dict[activity_type]:
                        if activity._Activity__grade_level == student._Student__grade_level:
                            activity._Activity__participants.append(student)
    
    for student in student_activity_list:
        if student.is_eligible():
            selected_activity = student._Student__selected_activity
            if selected_activity in activity_mapping:
                for activity_type in activity_mapping[selected_activity]:
                    for activity in act_dict[activity_type]:
                        if activity._Activity__grade_level == student._Student__grade_level:
                            activity._Activity__participants.append(student)
    
    for student in student_activity_list:
        if student.is_eligible():
            selected_activity = student._Student__selected_activity
            if selected_activity in activity_mapping:
                for activity_type in activity_mapping[selected_activity]:
                    for activity in act_dict[activity_type]:
                        if activity._Activity__grade_level == student._Student__grade_level:
                            activity._Activity__participants.append(student)
    
    for student in scholar_list:
        if student.is_eligible():
            selected_activity = student._Student__selected_activity.lower()
            if selected_activity in activity_mapping:
                for activity_type in activity_mapping[selected_activity]:
                    for activity in act_dict[activity_type]:
                        if (activity._Activity__grade_level == student._Student__grade_level) and (student not in activity._Activity__participants):
                            activity._Activity__participants.append(student)
    
    for student in artist_list:
        if student.is_eligible():
            selected_activity = student._Student__selected_activity.lower()
            if selected_activity in activity_mapping:
                for activity_type in activity_mapping[selected_activity]:
                    for activity in act_dict[activity_type]:
                        if (activity._Activity__grade_level == student._Student__grade_level) and (student not in activity._Activity__participants):
                            activity._Activity__participants.append(student)
    
    for student in athlete_list:
        if student.is_eligible():
            selected_activity = student._Student__selected_activity.lower()
            if selected_activity in activity_mapping:
                for activity_type in activity_mapping[selected_activity]:
                    for activity in act_dict[activity_type]:
                        if (activity._Activity__grade_level == student._Student__grade_level) and (student not in activity._Activity__participants):
                            activity._Activity__participants.append(student)
    '''
    for student in student_activity_list:
        if student._Student__selected_activity == "Sports":
            if student._Athlete__sports_category == "cricket":
                for act in act_dict["cricket"]:
                    if student.is_eligible() and act._Activity__grade_level == student._Student__grade_level:
                        act._Activity__participants.append(student)
            if student._Athlete__sports_category == "chess":
                for act in act_dict["chess"]:
                   if student.is_eligible() and act._Activity__grade_level == student._Student__grade_level:
                        act._Activity__participants.append(student)

        elif student._Student__selected_activity == "Academic":
            if student._Scholar__subject_specialization == "science":
                for act in act_dict["science"]:
                    if act._Activity__grade_level == student._Student__grade_level and student.is_eligible():
                        act._Activity__participants.append(student)

            elif student._Scholar__subject_specialization == "mathematics":
                for act in act_dict["mathematics"]:
                    if act._Activity__grade_level == student._Student__grade_level and student.is_eligible():
                        act._Activity__participants.append(student)

            elif student._Scholar__subject_specialization == "computers":
                for act in act_dict["computers"]:
                    if act._Activity__grade_level == student._Student__grade_level and student.is_eligible():
                        act._Activity__participants.append(student)
        
        elif student._Student__selected_activity == "Talent":
            for act in act_dict["blackrose"]:
                 if act._Activity__grade_level == student._Student__grade_level and student.is_eligible():
                        act._Activity__participants.append(student)

    # Set initial activity status based on participant count
    for activity_type in act_dict:
        for activity in act_dict[activity_type]:
            # Check if participants don't exceed max and there are at least 2
            if (activity._Activity__max_participants >= len(activity._Activity__participants)) and len(activity._Activity__participants) >= 2:
                activity._Activity__is_active = True
            else:
                activity._Activity__is_active = False
    
    # Special handling for team sports (cricket and chess)
    for activity_type in ["cricket", "chess"]:
        for activity in act_dict[activity_type]:
            if activity._SportsTournament__game_type == "Team":
                class_teams = {}
                for student in activity._Activity__participants:
                    team_key = student._Student__class_assigned
                    if team_key not in class_teams:
                        class_teams[team_key] = [student]
                    else:
                        class_teams[team_key].append(student)
                
                teams = list(class_teams.values())
                # For team sports, need at least 2 teams
                if len(teams) >= 2:
                    activity._Activity__is_active = True
                else:
                    activity._Activity__is_active = False
    
    # Update is_active using set_values for all activities
    '''
    for activity_type in act_dict:
        for activity in act_dict[activity_type]:
            activity.set_values({"is_active": activity._Activity__is_active})
    '''

    # Assign teachers as judges to activities
    for teacher in teacher_list:
        # Only assign teachers marked as judges
        if teacher._Teacher__judge:
            continue
        mentor_grade = teacher._Teacher__mentor_grade
        for activities in act_dict.values():
            for activity in activities:
                if activity._Activity__grade_level == mentor_grade:
                    activity._Activity__organizers.append(teacher)
                    # Mark teacher as assigned to prevent duplicate assignments
                    teacher._Teacher__judge = True

    # Update is_active flags using set_values [unchanged]
    for activity_type in act_dict:
        for activity in act_dict[activity_type]:
            activity.set_values({"is_active": activity._Activity__is_active})                        

   # Prepare the return lists - each will have 7 elements (one per grade)
    cricket_list, chess_list, mathematics_list , science_list, computers_list ,blackrose_list = act_dict["cricket"], act_dict["chess"], act_dict["mathematics"], act_dict["science"], act_dict["computers"], act_dict["blackrose"]
    a = [cricket_list, chess_list, mathematics_list, science_list, computers_list, blackrose_list]
    for ele in a:
        for j in ele:
            if j._Activity__max_participants < len(j._Activity__participants) or len(j._Activity__participants) < 2:
                j._Activity__is_active = False
            else:
                j._Activity__is_active = True
    
    return (cricket_list, chess_list, mathematics_list, science_list, computers_list, blackrose_list)


'''
a = register_activity("easy_participant_data.csv", "easy_activity_data1.csv")
for ele in a:
    for j in ele:
        print(j.__dict__)
'''

def winners(tuple):
    cricket_list, chess_list, mathematics_list, science_list, computers_list, blackrose_list = tuple
    grade = {6 :[], 7:[], 8:[] , 9:[], 10:[], 11:[], 12:[]}

    for i in tuple:
        for j in i:
            grade[j._Activity__grade_level].append(j)
    
    for key,val in grade.items():
        with open(f"grade{key}.csv", "w", newline ="") as file:
            writer = csv.DictWriter(file, fieldnames=["cricket", "chess", "mathematics", "science", "computers", "blackrose"])
            
            writer.writeheader()
            row_dict = {
                    "cricket": 'NA',
                    "chess": 'NA',
                    "mathematics": "NA",
                    "science": 'NA',
                    "computers": 'NA',
                    "blackrose": 'NA'
                }
            for i in val: 
                if i._Activity__is_active == True:
                    winner = i.determine_winner()
                    if winner == -1:
                        break
                    else:
                        row_dict[i.activity_name] = winner.idi
            writer.writerow(row_dict)


#sol = register_activity("easy_participant_data.csv", "easy_activity_data1.csv")
#winners(sol)
'''
a = [register_activity("easy_participant_data.csv", "easy_activity_data1.csv")]

for i in a:
    for j in i:
        for k in j:
            print(k.__dict__)
'''
