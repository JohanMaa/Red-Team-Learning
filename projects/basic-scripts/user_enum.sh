#!/bin/bash

echo "User dengan shell aktif di sistem:"
cat /etc/passwd | grep "/bin/bash"

