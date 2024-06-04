# school_data.py
# Bailey Collison
#
# A terminal-based application for computing and printing statistics based on given input.

import numpy as np
from given_data import year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022

class SchoolStats:
    """
    A class used to compue and print statistics for school enrollment data.
    Initializes the SchoolStats object with a dictionary that contains school names and codes and
    creates a 3D array from the given data file.

    """

    def __init__(self):

        self.school_id = {'Centennial High School':1224, 'Robert Thirsk School':1679, 'Louise Dean School':9626, 'Queen Elizabeth High School':9806,
                             'Forest Lawn High School':9813, 'Crescent Heights High School':9815, 'Western Canada High School':9816,
                             'Central Memorial High School':9823, 'James Fowler High School':9825, 'Ernest Manning High School':9826,
                             'William Aberhart High School':9829, 'National Sport School':9830, 'Henry Wise Wood High School':9836,
                             'Bowness High School':9847, 'Lord Beaverbrook High School':9850, 'Jack James High School':9856, 'Sir Winston Churchill High School':9857,
                             'Dr. E. P. Scarlett High School': 9858, 'John G Diefenbaker High School':9860, 'Lester B. Pearson High School':9865}
        
        # Creating a NymPy array using the imported data and reshaping it to a 3D array
        self.array = np.array([year_2013, year_2014, year_2015, year_2016, year_2017, year_2018, year_2019, year_2020, year_2021, year_2022])
        self.array = self.array.reshape(10, 20, 3)

    def school_id_index(self, school_selection):
        """
        Method that returns the index of a given school stored in the given_data.py file

        Paramaters: 
            school_selection (str or int): The school name or code selected

        Returns:
            i (int): The index of the school selected in the dictionary

        Raises:
            ValueError: When school name or code entered is not found in the dictionary

        """
        # Searching for school codes and if found, using enumerate to iterate over dictionary and keep index
        try:
            school_selection = int(school_selection)
            if school_selection in self.school_id.values():
                for i, code in enumerate(self.school_id.values()):
                    if code == school_selection:
                        return i
        except ValueError:
        # Searching for school names and if found, using enumerate to iterate over dictionary and keep index
            if school_selection in self.school_id:
                for i, name in enumerate(self.school_id.keys()):
                    if name == school_selection:
                        return i
        # raise ValueError if the school selection is not found in the names or codes
        raise ValueError("You must enter a valid school name or code.")
        
    def school_stats(self, school_selection):
        """
        Calculates multiple school statistics specific to the school selected using NumPy methods

        Parameters:
            school_selection (str or int): The school name or code selected

        No returns
        
        """
        # Extracts a 2D array containing all the year and grade data for the selected school
        school_data = self.array[:, self.school_id_index(school_selection), :]
        # Return the school name and code for the selected school
        school_name = list(self.school_id.keys())[self.school_id_index(school_selection)]
        school_code = list(self.school_id.values())[self.school_id_index(school_selection)]
        # Calculate the mean for each grade using the NumPy mean function on our 2D array
        grade_10_mean = int(np.nanmean(school_data[:, 0]))
        grade_11_mean = int(np.nanmean(school_data[:, 1]))
        grade_12_mean = int(np.nanmean(school_data[:, 2]))
        # Calculate the max and min grade using the NumPy max/min functions on our 2D array
        highest_enrollment = int(np.nanmax(school_data))
        lowest_enrollment = int(np.nanmin(school_data))
        #Initialize the enrollment over 10 years to 0
        enrollment_10_year = 0
        # Checking if there are any enrollments over 500 in the array and returning the median
        enrollments_over_500 = school_data[school_data > 500]
        if enrollments_over_500.size > 0:
            median_over_500 = int(np.median(enrollments_over_500))
        else:
            median_over_500 = 0

        # Printing the results corresponding to the sample output
        print("School Name: " + str(school_name) + ", School Code: " + str(school_code))
        print("Mean enrollment for grade 10: " + str(grade_10_mean))
        print("Mean enrollment for grade 11: " + str(grade_11_mean))
        print("Mean enrollment for grade 12: " + str(grade_12_mean))
        print("Highest enrollment for a single grade: " + str(highest_enrollment))
        print("Lowest enrollment for a single grade: " + str(lowest_enrollment))
        # Using a for loop over 10 years to calculate and print the enrollment for each year
        # as well as calculating the total enrollment over 10 years and its mean
        for i in range(10):
            yearly_enrollment = int(np.nansum(self.array[i, self.school_id_index(school_selection), :]))
            year = 2013 + i
            print("Total enrollment for " + str(year) + ": " + str(yearly_enrollment))
            enrollment_10_year += yearly_enrollment
            mean_total_enrollment = int(enrollment_10_year/(1+i))
        # Printing the rest of the results
        print("Total ten year enrollment: " + str(enrollment_10_year))
        print("Mean total enrollment over 10 years: " + str(mean_total_enrollment))
        print("For all enrollments over 500, the median value was: " + str(median_over_500))

    def general_stats(self):
        """
        Computes and prints multiple general statistics for all schools using NumPy methods
        
        No parameters or returns

        """
        # Calculate the mean enrollment of 2013 and 2022 using the NumPy mean function
        mean_2013_enrollment = int(np.nanmean(self.array[0, :, :]))
        mean_2022_enrollment = int(np.nanmean(self.array[-1, :, :]))
        # Calculate the total graduates for all schools in 2022 usinf the NumPy sum function
        total_grad_2022 = int(np.nansum(self.array[-1, :, 2]))
        # Calculate the total highest and lowest enrollment using the NumPy max/min functions
        highest_enrollment = int(np.nanmax(self.array))
        lowest_enrollment = int(np.nanmin(self.array))

        # Printing the results corresponding to the sample output
        print("Mean enrollment in 2013: " + str(mean_2013_enrollment))
        print("Mean enrollment in 2022: " + str(mean_2022_enrollment))
        print("Total graduating class of 2022: " + str(total_grad_2022))
        print("Highest enrollment for a single grade: " + str(highest_enrollment))
        print("Lowest enrollment for a single grade: " + str(lowest_enrollment))
        
def main():
    # Creating an object of the SchoolStats class called stats
    stats = SchoolStats()

    print("ENSF 692 School Enrollment Statistics")
    # Printing the shape and dimensions of our array
    print("Shape of full data array:", stats.array.shape)
    print("Dimensions of full data array:", stats.array.ndim)
    # Using a while true loop to prompt for re-entry without terminating the program
    while True:
        school_selection = input("Please enter the high school name or school code: ")
        try:
            stats.school_id_index(school_selection)
            break
        except ValueError as e:
            print(e)

    print("\n***Requested School Statistics***\n")
    # Using out inputted school selection on the school_stats function
    stats.school_stats(school_selection)

    print("\n***General Statistics for All Schools***\n")
    # Running the general_stats function that will be the same regardless of input
    stats.general_stats()

if __name__ == '__main__':
    main()

