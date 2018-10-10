from PyQt5.QtCore import (QEasingCurve, QPropertyAnimation, QRect, QTimer)
from PyQt5.QtGui import QPalette
import re


class AnimateMainButtons(object):
    def __init__(self, context):
        self.context = context
        self.index = list()
        self.alpha = 0
        self.animation_number = -1;

        self.context.btn_new_card.setStyleSheet('color: rgb(0,0,0,%s)' % 0)
        self.context.btn_checkout.setStyleSheet('color: rgb(0,0,0,%s)' % 0)
        self.context.btn_charge.setStyleSheet('color: rgb(0,0,0,%s)' % 0)
        self.context.btn_vip.setStyleSheet('color: rgb(0,0,0,%s)' % 0)
        self.context.btn_reports.setStyleSheet('color: rgb(0,0,0,%s)' % 0)

        self.init_button_animation()

    def initButtonGeometryAnimation(self, element, start, end, duration=500, loopcount=1):
        element.setStartValue(start)
        element.setEndValue(end)
        element.setDuration(duration)
        element.setLoopCount(loopcount)
        element.setEasingCurve(QEasingCurve.OutCurve)

    def init_button_animation(self):
        self.b_position = []
        self.b_position.append(
            self.animation_button_geometry(self.context.btn_new_card, self.context.btn_new_card.geometry()))
        self.b_position.append(
            self.animation_button_geometry(self.context.btn_checkout, self.context.btn_checkout.geometry()))
        self.b_position.append(
            self.animation_button_geometry(self.context.btn_charge, self.context.btn_charge.geometry()))
        self.b_position.append(self.animation_button_geometry(self.context.btn_vip, self.context.btn_vip.geometry()))
        self.b_position.append(
            self.animation_button_geometry(self.context.btn_reports, self.context.btn_reports.geometry()))

        self.timers = []
        for i in range(len(self.b_position)):
            self.timers.append(QTimer())
            self.timers[i].timeout.connect(self.start_moving)
            self.timers[i].setSingleShot(True)
            self.timers[i].start(i * 100)
        self.timer = QTimer()
        self.timer.timeout.connect(self.animation_button_alpha)
        self.timer.start(4)

    def start_moving(self):
        self.animation_number += 1
        self.b_position[self.animation_number].start()

        self.index.append(self.animation_number)

    def animation_button_geometry(self, element, pos):
        start_x = 0
        start_y = pos.y()
        start_width = pos.width()
        start_height = pos.height()
        start = QRect(start_x, start_y, start_width, start_height)
        end = pos

        self.anim = QPropertyAnimation(element, 'geometry'.encode())
        self.initButtonGeometryAnimation(self.anim, start=start, end=end)
        return self.anim

    def animation_button_alpha(self):
        if 0 in self.index:
            alpha = self.context.btn_new_card.palette().color(QPalette.Text).alpha()
            alpha += 1
            if alpha < 256:
                self.context.btn_new_card.setStyleSheet('color: rgb(0,0,0,%s)' % alpha)
        if 1 in self.index:
            alpha = self.context.btn_checkout.palette().color(QPalette.Text).alpha()
            alpha += 1
            if alpha < 256:
                self.context.btn_checkout.setStyleSheet('color: rgb(0,0,0,%s)' % alpha)
        if 2 in self.index:
            alpha = self.context.btn_charge.palette().color(QPalette.Text).alpha()
            alpha += 1
            if alpha < 256:
                self.context.btn_charge.setStyleSheet('color: rgb(0,0,0,%s)' % alpha)
        if 3 in self.index:
            alpha = self.context.btn_vip.palette().color(QPalette.Text).alpha()
            alpha += 1
            if alpha < 256:
                self.context.btn_vip.setStyleSheet('color: rgb(0,0,0,%s)' % alpha)
        if 4 in self.index:
            alpha = self.context.btn_reports.palette().color(QPalette.Text).alpha()
            alpha += 1
            if alpha < 256:
                self.context.btn_reports.setStyleSheet('color: rgb(0,0,0,%s)' % alpha)
            if alpha == 255:
                self.timer.disconnect()
