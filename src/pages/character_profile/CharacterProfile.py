import pygame
import sys
from pygame.locals import *

from src.components.Label import Label
from src.components.Button import Button
from src.components.CharacterEquipment import CharacterEquipment
from src.components.ItemGrid import ItemGrid
from src.components.PopupItem import PopupItem
from src.components.SwitchCards import SwitchCards
from src.components.Container import Container

from .Measurements import Measurements as meas

from src.globals.mock_data import character_2


def CharacterProfile(screen, mainClock):
    running = True
    curr_item_in_popup = ''
    backpack_active = 0
    active_item = -1

    def reloadButtons(buttons_list, current_active):
        newButtons = []

        for i in range(len(buttons_list)):
            if i == current_active:
                buttons_list[i].colorSchemes = meas.bt_class_active['color']
                buttons_list[i].color = meas.bt_class_active['color'].inactive
                buttons_list[i].path = meas.buttons_backpack['path_white']
                buttons_list[i].image = buttons_list[i].makeImage(meas.buttons_backpack['path_white'],
                                                                  meas.bt_class_active['image_offset'])
                buttons_list[i].border_radius = meas.bt_class_active['border_radius']
            else:
                buttons_list[i].colorSchemes = meas.bt_class_inactive['color']
                buttons_list[i].color = meas.bt_class_inactive['color'].inactive
                buttons_list[i].path = meas.buttons_backpack['path_gray']
                buttons_list[i].image = buttons_list[i].makeImage(meas.buttons_backpack['path_gray'],
                                                                  meas.bt_class_inactive['image_offset'])
                buttons_list[i].border_radius = meas.bt_class_inactive['border_radius']

            newButtons.append(buttons_list[i])

        return newButtons

    def reloadItemGrid(backpack_active):
        return ItemGrid(meas.ig_backpack['x'], meas.ig_backpack['y'],
                        meas.ig_backpack['item_size'], meas.ig_backpack['item_padding'],
                        meas.ig_backpack['cols'], meas.ig_backpack['amount'], screen,
                        meas.ig_backpack['backpack_ref'][backpack_active], active=active_item)

    label_page = Label(meas.label_page['text'], meas.label_page['font'], meas.label_page['color'],
                       screen, meas.label_page['x'], meas.label_page['y'], meas.label_page['anchor'])

    bt_return = Button(meas.bt_return['color'], meas.bt_return['x'], meas.bt_return['y'],
                       meas.bt_return['width'], meas.bt_return['height'], screen,
                       path=meas.bt_return['path'])

    ce_characterEqPreview = CharacterEquipment(meas.ce_characterEqPreview['x'],
                                               meas.ce_characterEqPreview['y'],
                                               meas.ce_characterEqPreview['font'],
                                               meas.ce_characterEqPreview['colors'],
                                               meas.ce_characterEqPreview['character_ref'],
                                               screen)

    ig_backpack = ItemGrid(meas.ig_backpack['x'], meas.ig_backpack['y'],
                           meas.ig_backpack['item_size'], meas.ig_backpack['item_padding'],
                           meas.ig_backpack['cols'], meas.ig_backpack['amount'], screen,
                           meas.ig_backpack['backpack_ref'][backpack_active], active=active_item)

    buttons_backpack = [Button(meas.bt_class_active['color'],
                               meas.buttons_backpack['x'], meas.buttons_backpack['y'] +
                                    i * (meas.buttons_backpack['height'] + meas.buttons_backpack['padding']),
                               meas.buttons_backpack['width'], meas.buttons_backpack['height'], screen,
                               path=meas.buttons_backpack['path_gray'],
                               image_ofset=meas.bt_class_active['image_offset'],
                               border_radius=meas.bt_class_active['border_radius'])
                        for i in range(len(meas.ig_backpack['backpack_ref']))]

    c_backpack = Container(meas.c_backpack['x'], meas.c_backpack['y'], meas.c_backpack['width'],
                           meas.c_backpack['height'], buttons_backpack + [ig_backpack])

    stats_headers = [
        Label(meas.labels_stats[i].capitalize(), meas.label_stat_header['font'], meas.label_stat_header['color'],
              screen, meas.label_stat_header['x'],
              meas.label_stat_header['y'] + i * (
                      meas.label_stat_header['height'] + meas.label_stat_header['padding']),
              meas.label_stat_header['anchor'])
        for i in range(len(meas.labels_stats))]

    stats_values = [Label(str(character_2['statistics'][meas.labels_stats[i]]), meas.label_stat_values['font'],
                          meas.label_stat_values['color'], screen, meas.label_stat_values['x'],
                          meas.label_stat_values['y'] + i * (
                                  meas.label_stat_values['height'] + meas.label_stat_values['padding']),
                          meas.label_stat_values['anchor'])
                    for i in range(len(meas.labels_stats))]

    c_stats = Container(meas.c_stats['x'], meas.c_stats['y'], meas.c_stats['width'], meas.c_stats['height'],
                        stats_headers + stats_values)

    sc_eq_stat = SwitchCards(meas.sc_eq_stat['x'], meas.sc_eq_stat['y'],
                             meas.sc_eq_stat['width'], meas.sc_eq_stat['height'], meas.sc_eq_stat['font'],
                             meas.sc_eq_stat['color'], screen, [c_backpack, c_stats], ['Items', 'Statistics'],
                             switch_height=meas.sc_eq_stat['switch_height'])

    ppi_itemDescription = PopupItem(0, 0, 100, 50, screen, '', meas.text_font)

    while running:
        screen.fill((255, 255, 255))
        pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        sc_eq_stat.components[0].components[-1] = reloadItemGrid(backpack_active)
        buttons_backpack = reloadButtons(buttons_backpack, backpack_active)

        label_page.draw()
        bt_return.draw()
        ce_characterEqPreview.draw()
        sc_eq_stat.draw()

        ppi_itemDescription.draw()

        mx, my = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            if event.type == MOUSEBUTTONDOWN:
                # LEFT CLICK
                if event.button == 1:
                    # HANDLE RETURN BUTTON
                    if bt_return.rect.collidepoint(event.pos):
                        running = False
                        print("Redirecting: CharacterProfile.py -> CityMap.py")

                    # CARD SWITCH
                    for i in range(len(sc_eq_stat.buttons)):
                        if sc_eq_stat.buttons[i].rect.collidepoint(event.pos):
                            sc_eq_stat.current = i
                            break

                    # EQ
                    for key in ce_characterEqPreview.character:
                        if type(ce_characterEqPreview.character[key]).__name__ == "ItemBox":
                            if ce_characterEqPreview.character[key].rect.collidepoint(event.pos):
                                print(key)

                    # ITEM GRID
                    c_backpack_elem = sc_eq_stat.components[0].components
                    for i in range(len(c_backpack_elem)):
                        # BACKPACKS
                        if type(c_backpack_elem[i]).__name__ == "Button":
                            if c_backpack_elem[i].rect.collidepoint(event.pos):
                                backpack_active = i
                                active_item = -1
                                break

                        # ACTIVATE ITEMS
                        else:
                            for j in range(len(c_backpack_elem[i].backpack_ref)):
                                if c_backpack_elem[i].backpack[j].rect.collidepoint(event.pos):
                                    if active_item == j:
                                        active_item = -1
                                    else:
                                        active_item = j
                                    # print(c_backpack_elem[i].backpack_ref[j]['name'])
                                    break

                # RIGHT CLICK
                if event.button == 3:
                    for i in range(len(ig_backpack.backpack_ref)):
                        if ig_backpack.backpack[i].rect.collidepoint(event.pos):
                            if curr_item_in_popup == ig_backpack.backpack_ref[i]['name']:
                                ppi_itemDescription = PopupItem(0, 0, 200, 80, screen,
                                                                '', meas.text_font)
                            else:
                                print('Here: ', ig_backpack.backpack_ref[i]['name'])
                                x = min(mx, meas.window_width - 200)
                                y = min(my, meas.window_height - 80)
                                ppi_itemDescription = PopupItem(x, y, 200, 80, screen,
                                                                ig_backpack.backpack_ref[i]['name'],
                                                                meas.text_font,
                                                                isVisible=True)
                                curr_item_in_popup = ig_backpack.backpack_ref[i]['name']
                            break

        pygame.display.update()
        mainClock.tick(60)
