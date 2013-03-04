#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2007-2013 PlayOnLinux Team

from views.Modal import Modal

class Message(Modal):
   def __init__(self, content): 
      self.title = _('Message')
      self.content = content
      self.show()