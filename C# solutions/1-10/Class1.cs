using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace Euler
{
    class Class1
    {
        public int taskid;
        // Inheritance
        public void GetTask(int id)
        {
            Console.WriteLine( "Task " + id );
        }
        public void SolveTask()
        {
            Console.WriteLine("Task 1 Solution");
        }
    }
}
