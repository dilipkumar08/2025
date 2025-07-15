import java.util.*;

//employee data in a object 
class Employee
{
	protected String name;
	protected double salary;
	protected String designation;
	protected String department;
	public  Employee(String name, double salary, String designation, String department)
	{
		this.name=name;
		this.salary=salary;
		this.designation=designation;
		this.department=department;
		
	}
}

//used to list all the employee data in the employee list
interface  list_manipulator
{
	 	
	void list_display();
	void list_remove_element(String employee_name);
	void list_add_element(String name, double salary, String designation, String department);
	void list_remove();

}

//this class if to manipulate 
class Employee_list implements list_manipulator
{
	protected List<Employee> employees_list= new ArrayList<>();
	protected int length=0;
	
	public Employee_list() {} //constructor

	@Override
	public void list_add_element(String name, double salary, String designation, String department)
	{
		Employee e = new Employee(name,salary,designation,department);
		employees_list.add(e);
		length+=1;
	}
	
	@Override // to display the elements in the list
	public void list_display() // displayer
	{
		Employee employee = null;
		if (length>=1)
		{
			System.out.println("looping in data to display");
			for(int index = 0; index<length; index++)
			{
				employee=employees_list.get(index);
				System.out.println("Employee name: "+employee.name);
				System.out.println("Employee designation: "+employee.designation);
				System.out.println("Employee Salary:"+employee.salary);
				System.out.println("Employee Department:"+employee.department);
				System.out.println("----------------------------------------------------------------------------------------");	
			}
		}
		else
		{
			System.out.println("There's no data to display. please enter some...");
		}
	}

	@Override //used to remove a particular element from the list based on the name
	public void list_remove_element(String employee_name)
	{
		 if(length<1)
		 {
			 System.out.println("list is empty...");
		 }
		 else
		 {
			System.out.println("not empty");
			boolean exist = false;
			for(int index = 0; index<length; index++)
			{
				System.out.println("checking..");
				if (employees_list.get(index).name.toLowerCase().equals(employee_name.toLowerCase()))
				{
					 System.out.println("found the employee to remove..");
					 employees_list.remove(index);
					 System.out.println("removing "+employee_name+"...");
					 exist=true;
					 break;
				}
			}
			if(exist!=true)
			{
				System.out.println("Employee does not exists..");
			}
		 }
	 
	}
	@Override // to delete the whole list
	public void list_remove() {
		employees_list.clear();
		System.out.println("Employees data cleared...");
		
	}
}

public class Inheritance {
	public static void main(String args[])
	{
		Scanner scanner = new Scanner(System.in);
		Employee_list lister = new Employee_list();
		int option=0;
		while(option>=0 && option<=4)
		{
			System.out.println("1. Insert\n2. Delete\n3. Display\n4. Clear List");
			System.out.println("Choose a options:");
			int temp = scanner.nextInt();
			scanner.nextLine();
			option=temp;
			if (option==1)
			{
				boolean success = false;
				while(!success)
				{
					try 
					{
						System.out.println("\t\tInserting...");
						System.out.println("Enter the name of the Employee: ");
						String name = scanner.nextLine();
			 
						System.out.println("Enter the designation of the Employee: ");
						String designation = scanner.nextLine();
			 
						System.out.println("Enter the salary of the Employee: ");
						double salary = scanner.nextDouble();
						scanner.nextLine();
			 
						System.out.println("Enter the department of the Employee: ");
						String department = scanner.nextLine();
						lister.list_add_element(name,salary,designation,department);
						success=true;
						}
					catch (Exception e)
					{
						System.out.println("Please, Enter the right values to the right fields");
					}
			 
				}
			}
			else if(option==2) // for deletion
			{
				System.out.println("\t\tDeleting...");
				System.out.println("Enter the name of Employee to be deleted: ");
				String delete_name = scanner.nextLine();
				lister.list_remove_element(delete_name);
			 
			} 
			else if (option==3) // for displaying
			{
				System.out.println("\t\tDisplaying...");
				lister.list_display(); 
				scanner.nextLine();
			}
		 
			else if (option==4) // for truncating
			{
				System.out.println("\t\tClearing...");
				lister.list_remove();
			}
	
		}
		scanner.close();
	}
}
