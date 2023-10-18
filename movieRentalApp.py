import movieStore

def Run():
    print("Movie Rental Store - Victor Magopat" )
    FlimZ = movieStore.MovieStore

FlimZ = movieStore.MovieStore
FlimZ.Store_Name = "MISSISSAUGA"
FlimZ.Num_Movies_Total = 1
FlimZ.Num_Movies_Ava = 1
FlimZ.Rental_Fee = 5
FlimZ.Late_Fee = 10


print(FlimZ.Store_Name, FlimZ.Num_Movies_Total, FlimZ.Num_Movies_Ava, FlimZ.Rental_Fee, FlimZ.Late_Fee)