from PyQt5 import QtWidgets, QtCore, Qt, QtGui


class InterfaceBar(QtWidgets.QWidget):
    """docstring for InterfaceBar"""
    WIDTH, HEIGHT = 474, 364+100
    GEOMETRY = Qt.QRect(0,0,WIDTH,HEIGHT)
    SPAN = 10
    WIDE = WIDTH - SPAN*2
    WIDE_HALF = (WIDTH-SPAN*(1+2))/2
    WIDE_FOURTH = (WIDTH-SPAN*(1+4))/4
    WIDE_FIFTH = (WIDTH-SPAN*(1+5))/5

    
    HEIGHT_LABEL = 13
    HEIGHT_GROUPBOX = 6*(HEIGHT_LABEL+SPAN)+SPAN
    GEOMETRY_TOP_0_0 = Qt.QRect(SPAN, SPAN, WIDE_FOURTH, HEIGHT_LABEL)
    GEOMETRY_TOP_0_1 = Qt.QRect(SPAN+(SPAN + WIDE_FOURTH)*1, GEOMETRY_TOP_0_0.y()-3, WIDE_FOURTH, HEIGHT_LABEL+6)
    GEOMETRY_TOP_0_2 = Qt.QRect(SPAN+(SPAN + WIDE_FOURTH)*2, GEOMETRY_TOP_0_0.y(),   WIDE_FOURTH, HEIGHT_LABEL)
    GEOMETRY_TOP_0_3 = Qt.QRect(SPAN+(SPAN + WIDE_FOURTH)*3, GEOMETRY_TOP_0_0.y()-3, WIDE_FOURTH, HEIGHT_LABEL+6)
    
    GEOMETRY_TOP_1_0 = Qt.QRect(SPAN, GEOMETRY_TOP_0_0.bottom() + 1 + SPAN, WIDE_FOURTH, HEIGHT_LABEL)
    GEOMETRY_TOP_1_1 = Qt.QRect(SPAN+(SPAN + WIDE_FOURTH)*1, GEOMETRY_TOP_1_0.y(),          WIDE_FOURTH, HEIGHT_LABEL)
    GEOMETRY_TOP_1_2 = Qt.QRect(SPAN+(SPAN + WIDE_FOURTH)*2, GEOMETRY_TOP_1_0.y(),          WIDE_FOURTH, HEIGHT_LABEL)
    GEOMETRY_TOP_1_3 = Qt.QRect(SPAN+(SPAN + WIDE_FOURTH)*3, GEOMETRY_TOP_1_0.y() - 3,      WIDE_FOURTH, HEIGHT_LABEL + 6) # 3 and 6 sets adjust for combo box
    
    GEOMETRY_TOP_2_0 = Qt.QRect(SPAN, GEOMETRY_TOP_1_0.bottom() + 1 + SPAN,  WIDE_FOURTH, HEIGHT_LABEL)
    GEOMETRY_TOP_2_1 = Qt.QRect(SPAN+(SPAN + WIDE_FOURTH)*1, GEOMETRY_TOP_2_0.y(),     WIDE_FOURTH, HEIGHT_LABEL)
    GEOMETRY_TOP_2_2 = Qt.QRect(SPAN+(SPAN + WIDE_FOURTH)*2, GEOMETRY_TOP_2_0.y(),     WIDE_FOURTH, HEIGHT_LABEL)
    GEOMETRY_TOP_2_3 = Qt.QRect(SPAN+(SPAN + WIDE_FOURTH)*3, GEOMETRY_TOP_2_0.y() - 3, WIDE_FOURTH, HEIGHT_LABEL + 6)

    GEOMETRY_TOP_3_0 = Qt.QRect(SPAN, GEOMETRY_TOP_2_0.bottom() + 1 + SPAN,  WIDE_FOURTH, HEIGHT_LABEL)
    GEOMETRY_TOP_3_1 = Qt.QRect(SPAN+(SPAN + WIDE_FOURTH)*1, GEOMETRY_TOP_3_0.y(),     WIDE_FOURTH, HEIGHT_LABEL)
    GEOMETRY_TOP_3_2 = Qt.QRect(SPAN+(SPAN + WIDE_FOURTH)*2, GEOMETRY_TOP_3_0.y(),     WIDE_FOURTH, HEIGHT_LABEL)
    GEOMETRY_TOP_3_3 = Qt.QRect(SPAN+(SPAN + WIDE_FOURTH)*3, GEOMETRY_TOP_3_0.y() - 3, WIDE_FOURTH, HEIGHT_LABEL + 6)

    GEOMETRY_GROUPBOX = Qt.QRect(SPAN-5, GEOMETRY_TOP_3_0.bottom()+1+SPAN -5 , WIDE+10, HEIGHT_GROUPBOX+10)
    
    GEOMETRY_GROUPBOX_0_0 = Qt.QRect(SPAN, GEOMETRY_GROUPBOX.y()+SPAN*2, WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_0_1 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*1, GEOMETRY_GROUPBOX_0_0.y(), WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_0_2 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*2, GEOMETRY_GROUPBOX_0_0.y(), WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_0_3 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*3, GEOMETRY_GROUPBOX_0_0.y(), WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_0_4 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*4, GEOMETRY_GROUPBOX_0_0.y(), WIDE_FIFTH, HEIGHT_LABEL)

    GEOMETRY_GROUPBOX_1_0 = Qt.QRect(SPAN, GEOMETRY_GROUPBOX_0_0.bottom()+1+SPAN, WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_1_1 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*1, GEOMETRY_GROUPBOX_1_0.y(), WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_1_2 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*2, GEOMETRY_GROUPBOX_1_0.y(), WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_1_3 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*3, GEOMETRY_GROUPBOX_1_0.y(), WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_1_4 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*4, GEOMETRY_GROUPBOX_1_0.y(), WIDE_FIFTH, HEIGHT_LABEL)

    GEOMETRY_GROUPBOX_2_0 = Qt.QRect(SPAN, GEOMETRY_GROUPBOX_1_0.bottom()+1+SPAN, WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_2_1 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*1, GEOMETRY_GROUPBOX_2_0.y(), WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_2_2 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*2, GEOMETRY_GROUPBOX_2_0.y(), WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_2_3 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*3, GEOMETRY_GROUPBOX_2_0.y(), WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_2_4 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*4, GEOMETRY_GROUPBOX_2_0.y(), WIDE_FIFTH, HEIGHT_LABEL)


    GEOMETRY_GROUPBOX_3_0 = Qt.QRect(SPAN, GEOMETRY_GROUPBOX_2_0.bottom()+1+SPAN, WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_3_1 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*1, GEOMETRY_GROUPBOX_3_0.y(), WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_3_2 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*2, GEOMETRY_GROUPBOX_3_0.y(), WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_3_3 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*3, GEOMETRY_GROUPBOX_3_0.y(), WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_3_4 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*4, GEOMETRY_GROUPBOX_3_0.y(), WIDE_FIFTH, HEIGHT_LABEL)

    GEOMETRY_GROUPBOX_4_0 = Qt.QRect(SPAN, GEOMETRY_GROUPBOX_3_0.bottom()+1+SPAN, WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_4_1 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*1, GEOMETRY_GROUPBOX_4_0.y(), WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_4_2 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*2, GEOMETRY_GROUPBOX_4_0.y(), WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_4_3 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*3, GEOMETRY_GROUPBOX_4_0.y(), WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_4_4 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*4, GEOMETRY_GROUPBOX_4_0.y(), WIDE_FIFTH, HEIGHT_LABEL)    

    GEOMETRY_GROUPBOX_5_0 = Qt.QRect(SPAN, GEOMETRY_GROUPBOX_4_0.bottom()+1+SPAN, WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_5_1 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*1, GEOMETRY_GROUPBOX_5_0.y(), WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_5_2 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*2, GEOMETRY_GROUPBOX_5_0.y(), WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_5_3 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*3, GEOMETRY_GROUPBOX_5_0.y(), WIDE_FIFTH, HEIGHT_LABEL)
    GEOMETRY_GROUPBOX_5_4 = Qt.QRect(SPAN+(SPAN + WIDE_FIFTH)*4, GEOMETRY_GROUPBOX_5_0.y(), WIDE_FIFTH, HEIGHT_LABEL)    

    GEOMETRY_REMOVE_BUTTON = Qt.QRect(SPAN + (SPAN + WIDE_FIFTH)*2, GEOMETRY_GROUPBOX.bottom()+1+SPAN - 3, WIDE_FIFTH, HEIGHT_LABEL+6)
    COMBO_TOP_BOTTOM_NUMBER_ITEMS = ["None", "Queue", "Cooldown", "Carrying Res.", "Resource Type", "Hit Points", "Maximal HP", "Attack Melee", "Attack Range", "Attack", "Armor", "Garrisoned Units", "Count (Aggr.)", "Selected (Aggr.)", "Total Attack (Aggr.)", "Total HP (Aggr.)"]


    COMBO_EXPAND_ITEMS = ["Down, Left",
                          "Down, Right",
                          "Left, Up",
                          "Left, Down",
                          "Up, Left",
                          "Up, Right",
                          "Right, Up",
                          "Right, Down"]

    def __init__(self, name, parent):
        super(InterfaceBar, self).__init__(parent)
        self.parent = parent
        self.icon_list = None
        self.setGeometry(InterfaceBar.GEOMETRY)


        self.w_label_name = QtWidgets.QLabel("Name:", self)
        self.w_label_name.setGeometry(InterfaceBar.GEOMETRY_TOP_0_0)
        self.w_text_name = QtWidgets.QLineEdit(name, self)
        self.w_text_name.setGeometry(InterfaceBar.GEOMETRY_TOP_0_1)
        self.w_text_name.textChanged.connect(self.rename_tab)

        """
        self.w_label_expand = QtWidgets.QLabel("Expand:", self)
        self.w_label_expand.setGeometry(InterfaceBar.GEOMETRY_TOP_0_2)
        self.w_combo_expand = QtWidgets.QComboBox(self)
        self.w_combo_expand.setGeometry(InterfaceBar.GEOMETRY_TOP_0_3)
        self.w_combo_expand.addItems(InterfaceBar.COMBO_EXPAND_ITEMS)
        self.w_combo_expand.setCurrentIndex(3)
        """
        self.w_checkbox_movable = QtWidgets.QCheckBox("Movable", self)
        self.w_checkbox_movable.setGeometry(InterfaceBar.GEOMETRY_TOP_1_0)
        self.w_checkbox_movable.stateChanged.connect(self.set_movable)

        self.w_checkbox_aggregate = QtWidgets.QCheckBox("Aggregate", self)
        self.w_checkbox_aggregate.setGeometry(InterfaceBar.GEOMETRY_TOP_1_1)
        self.w_label__top_number = QtWidgets.QLabel("Top Number:", self)
        self.w_label__top_number.setGeometry(InterfaceBar.GEOMETRY_TOP_1_2)
        self.w_combo_top_number = QtWidgets.QComboBox(self)
        self.w_combo_top_number.setGeometry(InterfaceBar.GEOMETRY_TOP_1_3)
        self.w_combo_top_number.addItems(InterfaceBar.COMBO_TOP_BOTTOM_NUMBER_ITEMS)

        self.w_checkbox_hidden = QtWidgets.QCheckBox("Hidden", self)
        self.w_checkbox_hidden.setGeometry(InterfaceBar.GEOMETRY_TOP_2_0)
        self.w_checkbox_hidden.stateChanged.connect(self.set_hidden)
        self.w_checkbox_idle_time = QtWidgets.QCheckBox("Show Idle Time", self)
        self.w_checkbox_idle_time.setGeometry(InterfaceBar.GEOMETRY_TOP_2_1)
        self.w_label__bottom_number = QtWidgets.QLabel("Bottom Number:", self)
        self.w_label__bottom_number.setGeometry(InterfaceBar.GEOMETRY_TOP_2_2)
        self.w_combo_bottom_number = QtWidgets.QComboBox(self)
        self.w_combo_bottom_number.setGeometry(InterfaceBar.GEOMETRY_TOP_2_3)
        self.w_combo_bottom_number.addItems(InterfaceBar.COMBO_TOP_BOTTOM_NUMBER_ITEMS)

        self.w_checkbox_idle_blink = QtWidgets.QCheckBox("Blink when Idle", self)
        self.w_checkbox_idle_blink.setGeometry(InterfaceBar.GEOMETRY_TOP_3_0)
        self.w_checkbox_idle_pulse = QtWidgets.QCheckBox("Pulse when Idle", self)
        self.w_checkbox_idle_pulse.setGeometry(InterfaceBar.GEOMETRY_TOP_3_1)
        self.w_label_idle = QtWidgets.QLabel("Blinking or Pulsing for:", self)
        self.w_label_idle.setGeometry(InterfaceBar.GEOMETRY_TOP_3_2)
        self.w_text_idle_time_for_blinkin = QtWidgets.QSpinBox(self)
        self.w_text_idle_time_for_blinkin.setGeometry(InterfaceBar.GEOMETRY_TOP_3_3)
        self.w_text_idle_time_for_blinkin.setMaximum(99999)
        self.w_text_idle_time_for_blinkin.setSuffix(" seconds")
        
        self.w_groupbox = QtWidgets.QGroupBox("Policy", self)
        self.w_groupbox.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX)
        self.w_checkbox_show_all_units = QtWidgets.QCheckBox("All Units", self)
        self.w_checkbox_show_all_units.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_0_0)
        self.w_checkbox_show_all_units.stateChanged.connect(self.policy)
        self.w_checkbox_show_civilians = QtWidgets.QCheckBox("Civilians", self)
        self.w_checkbox_show_civilians.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_0_1)
        self.w_checkbox_show_civilians.stateChanged.connect(self.policy)
        self.w_checkbox_show_villagers = QtWidgets.QCheckBox("Villagers", self)
        self.w_checkbox_show_villagers.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_0_2)
        self.w_checkbox_show_villagers.stateChanged.connect(self.policy)
        self.w_checkbox_show_military = QtWidgets.QCheckBox("Military", self)
        self.w_checkbox_show_military.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_0_3)
        self.w_checkbox_show_military.stateChanged.connect(self.policy)
        self.w_checkbox_show_trade_units = QtWidgets.QCheckBox("Trade Units", self)
        self.w_checkbox_show_trade_units.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_0_4)
        self.w_checkbox_show_trade_units.stateChanged.connect(self.policy)

        self.w_checkbox_show_food_vills = QtWidgets.QCheckBox("Food Vills", self)
        self.w_checkbox_show_food_vills.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_1_0)
        self.w_checkbox_show_food_vills.stateChanged.connect(self.policy)
        self.w_checkbox_show_wood_vills = QtWidgets.QCheckBox("Wood Vills", self)
        self.w_checkbox_show_wood_vills.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_1_1)
        self.w_checkbox_show_wood_vills.stateChanged.connect(self.policy)
        self.w_checkbox_show_gold_vills = QtWidgets.QCheckBox("Gold Vills", self)
        self.w_checkbox_show_gold_vills.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_1_2)
        self.w_checkbox_show_gold_vills.stateChanged.connect(self.policy)
        self.w_checkbox_show_stone_vills = QtWidgets.QCheckBox("Stone Vills", self)
        self.w_checkbox_show_stone_vills.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_1_3)
        self.w_checkbox_show_stone_vills.stateChanged.connect(self.policy)
        self.w_checkbox_show_fish_ships = QtWidgets.QCheckBox("Fish Ships", self)
        self.w_checkbox_show_fish_ships.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_1_4)
        self.w_checkbox_show_fish_ships.stateChanged.connect(self.policy)
        
        self.w_checkbox_show_monastries = QtWidgets.QCheckBox("Monastries", self)
        self.w_checkbox_show_monastries.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_2_0)
        self.w_checkbox_show_monastries.stateChanged.connect(self.policy)
        self.w_checkbox_show_stables = QtWidgets.QCheckBox("Stables", self)
        self.w_checkbox_show_stables.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_2_1)
        self.w_checkbox_show_stables.stateChanged.connect(self.policy)
        self.w_checkbox_show_archery_ranges = QtWidgets.QCheckBox("Archery R.", self)
        self.w_checkbox_show_archery_ranges.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_2_2)
        self.w_checkbox_show_archery_ranges.stateChanged.connect(self.policy)
        self.w_checkbox_show_barracks = QtWidgets.QCheckBox("Barracks", self)
        self.w_checkbox_show_barracks.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_2_3)
        self.w_checkbox_show_barracks.stateChanged.connect(self.policy)
        self.w_checkbox_show_siege_workshops = QtWidgets.QCheckBox("Siege W.", self)
        self.w_checkbox_show_siege_workshops.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_2_4)
        self.w_checkbox_show_siege_workshops.stateChanged.connect(self.policy)

        self.w_checkbox_show_castles = QtWidgets.QCheckBox("Castles", self)
        self.w_checkbox_show_castles.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_3_0)
        self.w_checkbox_show_castles.stateChanged.connect(self.policy)
        self.w_checkbox_show_docks = QtWidgets.QCheckBox("Docks", self)
        self.w_checkbox_show_docks.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_3_1)
        self.w_checkbox_show_docks.stateChanged.connect(self.policy)
        self.w_checkbox_show_lumber_camps = QtWidgets.QCheckBox("Lumber C.", self)
        self.w_checkbox_show_lumber_camps.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_3_2)
        self.w_checkbox_show_lumber_camps.stateChanged.connect(self.policy)
        self.w_checkbox_show_mining_camps = QtWidgets.QCheckBox("Mining C.", self)
        self.w_checkbox_show_mining_camps.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_3_3)
        self.w_checkbox_show_mining_camps.stateChanged.connect(self.policy)
        self.w_checkbox_show_mills = QtWidgets.QCheckBox("Mills", self)
        self.w_checkbox_show_mills.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_3_4)
        self.w_checkbox_show_mills.stateChanged.connect(self.policy)

        self.w_checkbox_show_markets = QtWidgets.QCheckBox("Markets", self)
        self.w_checkbox_show_markets.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_4_0)
        self.w_checkbox_show_markets.stateChanged.connect(self.policy)
        self.w_checkbox_show_blacksmiths = QtWidgets.QCheckBox("Blacksmiths", self)
        self.w_checkbox_show_blacksmiths.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_4_1)
        self.w_checkbox_show_blacksmiths.stateChanged.connect(self.policy)
        self.w_checkbox_show_universities = QtWidgets.QCheckBox("Universities", self)
        self.w_checkbox_show_universities.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_4_2)
        self.w_checkbox_show_universities.stateChanged.connect(self.policy)
        self.w_checkbox_show_town_centers = QtWidgets.QCheckBox("Town Center", self)
        self.w_checkbox_show_town_centers.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_4_3)
        self.w_checkbox_show_town_centers.stateChanged.connect(self.policy)
        self.w_checkbox_show_towers = QtWidgets.QCheckBox("Towers", self)
        self.w_checkbox_show_towers.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_4_4)
        self.w_checkbox_show_towers.stateChanged.connect(self.policy)

        self.w_checkbox_show_constructions = QtWidgets.QCheckBox("Construct.", self)
        self.w_checkbox_show_constructions.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_5_0)
        self.w_checkbox_show_constructions.stateChanged.connect(self.policy)
        self.w_checkbox_show_selected = QtWidgets.QCheckBox("Selected", self)
        self.w_checkbox_show_selected.setGeometry(InterfaceBar.GEOMETRY_GROUPBOX_5_1)
        self.w_checkbox_show_selected.stateChanged.connect(self.policy)

        self.w_button_remove = QtWidgets.QPushButton("Remove", self)
        self.w_button_remove.setGeometry(InterfaceBar.GEOMETRY_REMOVE_BUTTON)
        self.w_button_remove.clicked.connect(self.remove)

    def remove(self):
        self.icon_list.deleteLater()
        self.deleteLater()

    def set_movable(self):
        self.icon_list.set_movable(self.w_checkbox_movable.isChecked())
        self.icon_list.raise_()

    def set_hidden(self):
        if self.w_checkbox_hidden.isChecked():
            self.icon_list.setVisible(False)
        else:
            self.icon_list.setVisible(True)
            #self.icon_list.show()
        

    def rename_tab(self):
        for index in range(self.parent.w_tabs_settings.count()):
            if self == self.parent.w_tabs_settings.widget(index):
                self.parent.w_tabs_settings.setTabText(index, self.w_text_name.text())

    def policy(self):
        result = set()
        player = self.parent.game.pov
        if self.w_checkbox_show_all_units.isChecked():
            result.update(set(player.units))
        if self.w_checkbox_show_civilians.isChecked():
            result.update(set(player.civilians))
        if self.w_checkbox_show_villagers.isChecked():
            result.update(set(player.villagers))
        if self.w_checkbox_show_military.isChecked():
            result.update(set(player.military))
        if self.w_checkbox_show_trade_units.isChecked():
            result.update(set(player.trade))
        if self.w_checkbox_show_food_vills.isChecked():
            result.update(set(player.vill_food))
        if self.w_checkbox_show_wood_vills.isChecked():
            result.update(set(player.vill_wood))
        if self.w_checkbox_show_gold_vills.isChecked():
            result.update(set(player.vill_gold))
        if self.w_checkbox_show_stone_vills.isChecked():
            result.update(set(player.vill_stone))
        if self.w_checkbox_show_fish_ships.isChecked():
            result.update(set(player.fish))
        if self.w_checkbox_show_monastries.isChecked():
            result.update(set(player.monastery))
        if self.w_checkbox_show_stables.isChecked():
            result.update(set(player.stables))
        if self.w_checkbox_show_archery_ranges.isChecked():
            result.update(set(player.archery))
        if self.w_checkbox_show_barracks.isChecked():
            result.update(set(player.barracks))
        if self.w_checkbox_show_siege_workshops.isChecked():
            result.update(set(player.siege))
        if self.w_checkbox_show_castles.isChecked():
            result.update(set(player.castle))
        if self.w_checkbox_show_docks.isChecked():
            result.update(set(player.docks))
        if self.w_checkbox_show_lumber_camps.isChecked():
            result.update(set(player.lumber_camps))
        if self.w_checkbox_show_mining_camps.isChecked():
            result.update(set(player.mining_camps))
        if self.w_checkbox_show_mills.isChecked():
            result.update(set(player.mill))
        if self.w_checkbox_show_markets.isChecked():
            result.update(set(player.market))
        if self.w_checkbox_show_blacksmiths.isChecked():
            result.update(set(player.blacksmiths))
        if self.w_checkbox_show_universities.isChecked():
            result.update(set(player.university))
        if self.w_checkbox_show_town_centers.isChecked():
            result.update(set(player.town_centers))
        if self.w_checkbox_show_towers.isChecked():
            result.update(set(player.towers))
        if self.w_checkbox_show_constructions.isChecked():
            result.update(set(player.constructions))
        if self.w_checkbox_show_selected.isChecked():
            result.update(set(player.selected))
        self.icon_list.game_obj = list(result)





if __name__ == '__main__':
    import bartender
        

