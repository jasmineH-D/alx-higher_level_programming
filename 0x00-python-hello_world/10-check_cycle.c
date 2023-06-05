#include "lists.h"

/**
 * check_cycle - checks if a linked list loops
 * @list: linked list
 * Return: 1 if linked list loops, 0 if it doesn't
 */

int check_cycle(listint_t *list)
{
	listint_t *lentgh = list;
	listint_t *rap = list;

	if (!list)
		return (0);

	while (rap != NULL && rap->next != NULL)
	{
		lentgh = lentgh->next;
		rap = rap->next->next;

		if (lentgh == rap)
			return (1);
	}
	return (0);
}
