import movieStore

def Run():
    print("Movie Rental Store - Victor Magopat" )


FlimZ = movieStore.MovieStore
FlimZ.Store_Name = "MISSISSAUGA"
FlimZ.Num_Movies = 1
FlimZ.Rental_Fee = 5
FlimZ.Late_Fee = 10

print(FlimZ.Store_Name, FlimZ.Num_Movies, FlimZ.Rental_Fee, FlimZ.Late_Fee)