from .defences import *
from .turrets import *
from .attackers import *
from .btns import *
from .general import *

from .shared import ImageAssets

Images = ImageAssets()
Images.add_image("page_btn_img", PageBtnImg)
Images.add_image("defence_center_img", DefenceCenterImg)
Images.add_image("attack_center_img", AttackCenterImg)
Images.add_image("blue_add_img", BlueAddImg)

Images.add_image("barracade_img", BarracadeImg)
Images.add_image("basic_turret_img", BasicTurretImg)
Images.add_image("spitter_img", SpitterImg)

Images.add_image("scoutship_img", ScoutShipImg)
Images.add_image("red_ship_img", RedShipImg)
Images.add_image("flee_ship_img", FleeShipImg)
Images.add_image("cargo_ship_img", CargoShipImg)
