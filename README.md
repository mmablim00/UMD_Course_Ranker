# UMD_Course_Ranker
CourseRanker is a tool that ranks University of Maryland (UMD) courses taught by specific instructors based on those instructors' grade data. Courses with certain instructors that have higher average GPA's are ranked higher.

Utilizes grade data for specific instructors/courses from the **PlanetTerp API**: https://api.planetterp.com/#planetterp-api

Also utilizes ethan-schaffer and saewitz's **Python Wrapper Class for the PlanetTerp API**: https://github.com/Planet-Terp/PlanetTerp-API-Python-Wrapper 

## Dependencies
* The PlanetTerp class uses the `requests` and `json` packages. One or both of these may already be installed for you. To install them to your computer, use something like `pip3` or `brew`.

* Python3

## Running CourseRanker
1. Clone or download this repository
2. Run the following command in the terminal:  `python3 CourseRanker.py`
