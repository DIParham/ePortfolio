package jUnitTesting;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.Test;

import module4.Task;

class TaskTest {

	@Test
	void testTask() {
		Task task = new Task("12345", "Java","All about programming");
		assertTrue(task.getTaskID().equals("12345"));
		assertTrue(task.getTaskName().equals("Java"));
		assertTrue(task.getTaskDes().equals("All about programming"));
	}
	@Test
	void testTaskIfNull() {
		Assertions.assertThrows(IllegalArgumentException.class, ()->{
			new Task(null, null, null);
		});
	}
	@Test
	void testTaskIf2Long() {
		Assertions.assertThrows(IllegalArgumentException.class, ()->{
			new Task( "12345678901", "java", "All about programming");
		});
	}

}
