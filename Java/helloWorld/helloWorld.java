// Use Pascal for Class Names
// Program Filename: The name of the program file should match the class name exactly.
// When saving the file, you should save it using the class name (remember, Java is case sensitive) and append .java as the filetype. If you have a class named MyFirstJavaProgram, then the file should be saved as MyFirstJavaProgram.java.
public class helloWorld {
    // Intrepetor will look for Entry Point: a method called Main which will handle the entire Java program
    // Method Names: All method names should start with a lower case letter. If there are multiple words in the method, they should be written in lowerCamelCase. Typically, we use verbs as method names, rather than noun statements.
    // Mandatory Method: Java program processing starts from the main() method which is a mandatory part of every executable Java program. It should look like this:
    public static void main(String[] args) {
        // Void: is return type of method: Void means we're not returning anything: if needed to return, change 'void' to 'string' | void: indicates that the main() method doesn't return anything.
        // System: is class that comes with all Java programs
        //static: means that the method belongs to and is called from the class itself rather than from an instance of the class.
        // public: This is known as an access modifier. Any public method we write is accessible from any other class or method in our project.
        // Out: is variable of class
        System.out.println("Hello World!");
        // return "Hello World";
    }
}