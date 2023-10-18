


class MovieStore:
    def __init__(self, Store_Name, Num_Movies_Total, Num_Movies_Ava, Rental_Fee, Late_Fee):
        self.Store_Name = Store_Name
        self.Num_Movies_Total = Num_Movies_Total
        self.Num_Movies_Ava = Num_Movies_Ava
        self.Rental_Fee = Rental_Fee
        self.Late_Fee = Late_Fee

    def bigger_then_zero(number):
        if number >= 0:
            Value = True
        else:
            Value = False
        return Value

    def Set_Name():
        name = input("What is the name of the store: ")
        MovieStore.Store_Name = name

    def Set_Total_Movies():
        while True:
            total_movies = input("Please input the number of Movies: ")
            total_movies = int(total_movies)
            Is_Biger = MovieStore.bigger_then_zero(total_movies)
            if Is_Biger == True:
                MovieStore.Num_Movies_Total = total_movies
                break
            else:
                print("please input a number bigger than zero.")
        
    def Set_Avalible_Movies():
        while True:
            movies_Available = input("Please input the number of Movies Available: ")
            movies_Available = int(movies_Available)
            Is_Biger = MovieStore.bigger_then_zero(movies_Available)
            if Is_Biger == True:
                MovieStore.Num_Movies_Ava = movies_Available
                break
            else:
                print("please input a number bigger than zero.")


    def Set_rental_Fee():
        while True:
            rent_cost = input("Please input the cost of renting: ")
            rent_cost = int(rent_cost)
            Is_Biger = MovieStore.bigger_then_zero(rent_cost)
            if Is_Biger == True:
                MovieStore.Rental_Fee = rent_cost
                break
            else:
                print("please input a number bigger than zero.")

    def Set_Late_Fee():
        while True:
            late_fee = input("Please input late fee: ")
            late_fee = int(late_fee)
            Is_Biger = MovieStore.bigger_then_zero(late_fee)
            if Is_Biger == True:
                MovieStore.Late_Fee = late_fee
                break
            else:
                print("please input a number bigger than zero.")


    def get_Name(MovieStore):
        print("the name of the film store is", MovieStore.Store_Name)

    def get_Total_Movies(MovieStore):
        print("the number of movies total is", MovieStore.Num_Movies_Total)

    def get_Avalible_Movies(MovieStore):
        print("the number of movies available is", MovieStore.Num_Movies_Ava)

    def get_rental_Fee(MovieStore):
        print("the rent cost is", MovieStore.Rental_Fee)

    def get_Late_Fee(MovieStore):
        print("the late fee per day is", MovieStore.Late_Fee)

    def calculateLateFee(days_late, MovieStore):
        late_fee_total = days_late * MovieStore.Late_Fee
        return late_fee_total

    def rentMovie(MovieStore):
        if MovieStore.Num_Movies_Ava > 0:
            MovieStore.Num_Movies_Ava = MovieStore.Num_Movies_Ava - 1
            return True
        else: 
            print("no movies to rent")
            return False

    def returnmovie(days_rented, MovieStore):
        MovieStore.Num_Movies_Ava = MovieStore.Num_Movies_Ava + 1
        if days_rented >= 4:
            days_late = days_rented - 3
            cost = MovieStore.calculateLateFee(days_late, MovieStore)
            print("you are ", days_late, "days late" )
            print("you must pay ", cost)
        else:
            print("Thank you for returning the movie.")