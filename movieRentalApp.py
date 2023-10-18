import movieStore

def Run():
    print("Movie Rental Store - Victor Magopat" )
    moviestore_1 = movieStore.MovieStore
    moviestore_1.Set_Name()
    moviestore_1.Set_Total_Movies()
    moviestore_1.Set_Avalible_Movies()
    moviestore_1.Set_rental_Fee()
    moviestore_1.Set_Late_Fee()
    moviestore_1.get_Name(moviestore_1)
    moviestore_1.get_Total_Movies(moviestore_1)
    moviestore_1.get_Avalible_Movies(moviestore_1)
    moviestore_1.get_rental_Fee(moviestore_1)
    moviestore_1.get_Late_Fee(moviestore_1)

Run()