# grofers-assignment
- Deployed on Heroku Cloud Service
- **Tech stack used : python, django rest framework, postgres, heroku**
- App Link https://my-assignment11.herokuapp.com/api/slot/2 
*(In the end of the api uri the number indicates slot number to allocate orders)*
- [x] API Documentation link : https://documenter.getpostman.com/view/4374691/TzmBCtc7

## Steps to run and execute a program in local
- Clone the Repository
- Execute python manage.py runserver in cmd it opens local host : http://127.0.0.1:8000/-
- if you want to use local db settings change the configuration in settings.py default its using aws postgres
- Open the post man and request the URI as shown in the documention link


## Schemas
## Table Name : Availability
| slot_id(pk)   | Vehicle Availability |
| ------------- | ------------- |
| slot value  | vehicles available in this slot  |

1. slot 1 -> (6-9)
2. slot 2 -> (9-13)
3. slot 3 -> (16-19)
4. slot 4 -> (19-23)

## Table Name : Capacity
| vehicle_id(pk)   | Vehicle Capacity |
| ------------- | ------------- |
| vehicled id  | capacity of the vehicle  |


## Table Name : VehiclesPerDay
| vehicle_id(pk)   | Vehicle type | vehicle count per day |
| ------------- | ------------- | ----------------------- |
| vehicled id  | type of the vehicle  | for this particular type how many vehicles are available per day |


https://github.com/Kasula11/grofers-assignment/blob/df2ff4c4713aa313424c1b9305bebbfdc90cf9f0/restapi/views.py#L51-L72
