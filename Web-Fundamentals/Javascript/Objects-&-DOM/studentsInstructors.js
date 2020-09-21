/*
Part I

Given the following array of objects:

var students = [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
]
Create a program that outputs:

Michael Jordan
John Rosales
Mark Guillen
KB Tonel
Part II (Optional)

Now, given the following dictionary:

var users = {
 'Students': [ 
     {first_name:  'Michael', last_name : 'Jordan'},
     {first_name : 'John', last_name : 'Rosales'},
     {first_name : 'Mark', last_name : 'Guillen'},
     {first_name : 'KB', last_name : 'Tonel'}
  ],
 'Instructors': [
     {first_name : 'Michael', last_name : 'Choi'},
     {first_name : 'Martin', last_name : 'Puryear'}
  ]
 }
Create a program that prints  the following format (including the number of characters in each combined name):

Students
1 - MICHAEL JORDAN - 13
2 - JOHN ROSALES - 11
3 - MARK GUILLEN - 11
4 - KB TONEL - 7
Instructors
1 - MICHAEL CHOI - 11
2 - MARTIN PURYEAR - 13
*/

// Students and Instructors
// Part 1
// var students = [ 
//     {first_name:  'Michael', last_name : 'Jordan'},
//     {first_name : 'John', last_name : 'Rosales'},
//     {first_name : 'Mark', last_name : 'Guillen'},
//     {first_name : 'KB', last_name : 'Tonel'}
// ]

// for(student in students){
//     console.log(students[student].first_name, students[student].last_name);
// }

// Part 2
var users = {
    'Students': [ 
        {first_name:  'Michael', last_name : 'Jordan'},
        {first_name : 'John', last_name : 'Rosales'},
        {first_name : 'Mark', last_name : 'Guillen'},
        {first_name : 'KB', last_name : 'Tonel'}
    ],
    'Instructors': [
        {first_name : 'Michael', last_name : 'Choi'},
        {first_name : 'Martin', last_name : 'Puryear'}
    ]
}

for(arr in users){
    console.log(arr);
    for(var i = 0; i < users[arr].length; i++){
        var fullname = users[arr][i].first_name + users[arr][i].last_name;
        console.log(`${i + 1} - ${users[arr][i].first_name} ${users[arr][i].last_name} - ${fullname.length}`);
    }
}