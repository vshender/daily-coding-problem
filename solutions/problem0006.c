/**
 * Problem #6 [Hard]
 *
 * This problem was asked by Google.
 *
 * An XOR linked list is a more memory efficient doubly linked list. Instead of
 * each node holding `next` and `prev` fields, it holds a field named `both`,
 * which is an XOR of the next node and the previous node. Implement an XOR
 * linked list; it has an `add(element)` which adds the element to the end, and
 * a `get(index)` which returns the node at index.
 *
 * If using a language that has no pointers (such as Python), you can assume
 * you have access to `get_pointer` and `dereference_pointer` functions that
 * converts between nodes and memory addresses.
 */

#include <assert.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>


typedef struct {
  int data;
  uintptr_t both;
} xor_node_t;

typedef struct {
  xor_node_t *head;
  xor_node_t *tail;
} xor_list_t;


/** Create an empty XOR linked list. */
xor_list_t *
xor_list_create(void)
{
  return (xor_list_t *)calloc(1, sizeof(xor_list_t));
}

/** Add an item to a XOR linked list. */
void
xor_list_add(xor_list_t *list, xor_node_t *node)
{
  node->both = (uintptr_t)list->tail;

  if (!list->head) {
    list->head = node;
    list->tail = node;
  } else {
    list->tail->both ^= (uintptr_t)node;
    list->tail = node;
  }
}

/** Get a XOR linked list's node at the given index. */
xor_node_t *
xor_list_get(xor_list_t *list, int index)
{
  if (index < 0) {
    return NULL;
  }

  xor_node_t *node = list->head;
  uintptr_t prev_addr = 0;

  for (; node && index > 0; --index) {
    uintptr_t next_addr = node->both ^ prev_addr;
    prev_addr = (uintptr_t)node;
    node = (xor_node_t *)next_addr;
  }

  return node;
}

/** Print the `n` first elements of a XOR linked list. */
void
debug_output(xor_list_t *list, int n)
{
  for (int i = 0; i < n; i++) {
    xor_node_t *node = xor_list_get(list, i);
    printf("list[%d] => ", i);
    if (node) {
      printf("%d\n", node->data);
    } else {
      printf("none\n");
    }
  }
}

int
main(void)
{
  xor_list_t *list = xor_list_create();
  assert(list);

  printf("iter #0:\n");
  debug_output(list, 3);

  for (int i = 1; i <= 3; ++i) {
    xor_node_t *node = (xor_node_t *)malloc(sizeof(xor_node_t));
    assert(node);

    node->data = i;
    xor_list_add(list, node);

    printf("\niter #%d:\n", i);
    debug_output(list, 3);
  }

  assert(xor_list_get(list, 0)->data == 1);
  assert(xor_list_get(list, 1)->data == 2);
  assert(xor_list_get(list, 2)->data == 3);
  assert(xor_list_get(list, 3) == NULL);

  return 0;
}
