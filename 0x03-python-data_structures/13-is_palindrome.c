#include "lists.h"

/**
 * is_palindrome - checks if a singly linked list is a
 * palindrome
 * @head: head of the linked list
 *
 * Return: 0 if not a palindrome, 1 if it is.
 */

int is_palindrome(listint_t **head)
{
	listint_t *temp;
	int array[3000];
	int i, counter = 0, half = 0;

	if (*head && (*head)->next)
	{
		temp = *head;
		while (temp)
		{
			array[counter] = temp->n;
			temp = temp->next;
			counter++;
		}
		counter--;
		half = (counter / 2) + 1;
		temp = *head;
		for (i = 0; i <= half; i++)
		{
			if (temp->n != array[counter])
				return (0);
			counter--;
			temp = temp->next;
		}
	}
	return (1);
}
