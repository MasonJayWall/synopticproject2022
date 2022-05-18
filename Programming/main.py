#########################################
#           Synoptic Project            #
#              Mason Wall               #
#########################################

from tkinter import *
import tkinter, sqlite3
from typing import final
from unittest import result
from PIL import ImageTk, Image

# Floating Variables
VERSION = '1.00'
AUTO_RESOLUTION = False
RESOLUTION = [1280,720]
DIAGNOSTICS = True

# Screen Mode | 1 - Home | 2 - Gender | 3 - Brand | 4 - Product Type | 5 - Results |
SCREEN_MODE = 1

# Interface Variables
APP_TITLE = ("Stylish You - Stock Management System | VERSION: %s" % (VERSION))

########################################################
# Instances                                            #
########################################################

colours = ["#ffffff", "#000000", "#011627", "#2eb4c6", "#e71d36", "#ff9f1c", "#eaeaea", "#c4c4c4", "#6d6d6d"]
genders = ["Mens", "Ladies", "Boys", "Girls"]
gfiles = ["StylishYou_Logo_Green", "StylishYou_Logo_Main", "StylishYou_Logo_Orange", "StylishYou_Logo_Red", "WeDevelopNow_logo"]

# Search Compilation | 0 - Gender | 1 - Product Type | 2 - Size | 3 - Colour | 4 - Price Min | 5 - Price Max | 6 - Brand | 
run_search = ["", "", "", "", "", "", ""]

class e:
    # Colours
    ultraWhite, ultraBlack, mainStyle, greenStyle, redStyle, orangeStyle, lightGrey, mediumGrey, greyText = range(9)

########################################################
# Dropdown Options                                     #
########################################################

#gender, brand, product_type, colour, size

gender_options = ["Mens", "Ladies", "Boys", "Girls"]
brand_options = ["Brand A", "Brand B", "Brand C", "Brand D"]
product_type_options = ["Fleeces", "Hoodies", "Dresses & Skirts", "Leggings & Tights", "Sweatshirts", "Polo Shirts", "Shoes", "Shorts", "Tracksuit Bottoms"]
colour_options = ["Beige", "Red", "Blue", "Tan", "Pink", "Multi", "Black", "Pink", "Purple"]
clothing_size_options = ["S", "M", "L", "XL", "XXL", "6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "12", "13"]
shoe_size_options = ["6", "6.5", "7", "7.5", "8", "8.5", "9", "9.5", "10", "10.5", "11", "12", "13"]

########################################################
# Compile Interface Elements                           #
########################################################

# Element tipes | 1 - Create | 2 - Show | 3 - Hide |

#----------------------------------------------------

def setup_tk():
    global mainWindow, RESOLUTION, APP_TITLE, productTypeSelected, sizeSelected, colourSelected, brandSelected, genderSelected
    mainWindow = Tk()

    # Detect & Set Resolution
    if AUTO_RESOLUTION:
        screen_width, screen_height = mainWindow.winfo_screenwidth(), mainWindow.winfo_screenheight()
        RESOLUTION = [screen_width, screen_height]

    mainWindow.geometry("%dx%d" % (RESOLUTION[0], RESOLUTION[1]))
    APP_TITLE = ("%s | %d x %d_" % (APP_TITLE, RESOLUTION[0], RESOLUTION[1]))

    mainWindow.resizable(False, False)
    mainWindow.title(APP_TITLE)
    mainWindow.configure(background = colours[e.ultraWhite])

    productTypeSelected = StringVar()
    sizeSelected = StringVar()
    colourSelected = StringVar()
    brandSelected = StringVar()
    genderSelected = StringVar()

    productTypeSelected.set("Product Type")
    sizeSelected.set("Size")
    colourSelected.set("Colour")
    brandSelected.set("Brand")
    genderSelected.set("Gender")

    home_menu(1)

#----------------------------------------------------

def home_menu(tipe):
    global homeCanvas, SCREEN_MODE, productTypeSelected, sizeSelected, colourSelected, brandSelected, genderSelected, genderMinimumPriceEntry, genderMaximumPriceEntry, brandMinimumPriceEntry, brandMaximumPriceEntry, typeMinimumPriceEntry, typeMaximumPriceEntry

    if tipe == 1:
        global RESOLUTION
        RESOLUTION = [400, 700]
        mainWindow.geometry("400x700")

        if DIAGNOSTICS: print('CREATE: Home Screen')

        homeCanvas = Canvas(mainWindow, width = RESOLUTION[0], height = RESOLUTION[1], bd = 0, highlightthickness = 0, background = colours[e.ultraWhite])
        topFrame = Frame(homeCanvas, bg = colours[e.mainStyle], width = 400, height = 100)

        mensButton = Button(homeCanvas, width = 20, height = 10, bd = 0, text = 'MENS', font = ('Arial Black', 8), bg = colours[e.mainStyle], fg = colours[e.ultraWhite], command = lambda: search_by_gender(2, 0))
        ladiesButton = Button(homeCanvas, width = 20, height = 10, bd = 0, text = 'LADIES', font = ('Arial Black', 8), bg = colours[e.mainStyle], fg = colours[e.ultraWhite], command = lambda: search_by_gender(2, 1))

        boysButton = Button(homeCanvas, width = 20, height = 10, bd = 0, text = 'BOYS', font = ('Arial Black', 8), bg = colours[e.mainStyle], fg = colours[e.ultraWhite], command = lambda: search_by_gender(2, 2))
        girlsButton = Button(homeCanvas, width = 20, height = 10, bd = 0, text = 'GIRLS', font = ('Arial Black', 8), bg = colours[e.mainStyle], fg = colours[e.ultraWhite], command = lambda: search_by_gender(2, 3))

        brandButton = Button(homeCanvas, width = 20, height = 10, bd = 0, text = 'BRAND', font = ('Arial Black', 8), bg = colours[e.mainStyle], fg = colours[e.ultraWhite], command = lambda: search_by_brand(2))
        typeButton = Button(homeCanvas, width = 20, height = 10, bd = 0, text = 'PRODUCT TYPE', font = ('Arial Black', 8), bg = colours[e.mainStyle], fg = colours[e.ultraWhite], command = lambda: search_by_type(2))

        mensButton.place(relx = 0.25, rely = 0.2, anchor = N)
        ladiesButton.place(relx = 0.75, rely = 0.2, anchor = N)

        boysButton.place(relx = 0.25, rely = 0.45, anchor = N)
        girlsButton.place(relx = 0.75, rely = 0.45, anchor = N)

        brandButton.place(relx = 0.25, rely = 0.7, anchor = N)
        typeButton.place(relx = 0.75, rely = 0.7, anchor = N)

        # Load Logo

        stylishYouMain = Image.open("graphics/StylishYou_Logo_Main.png")
        stylishYouMain = stylishYouMain.resize((80, 80))
        stylishYouMain = ImageTk.PhotoImage(stylishYouMain)

        stylishYouMain_Label = Label(topFrame, image=stylishYouMain, bd = 0)
        stylishYouMain_Label.image = stylishYouMain

        stylishYouMain_Label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        for i in range(2):
            [homeCanvas, topFrame][i].place(relx = 0.5, rely = [0, 0][i], anchor = N)

        # Create other Screens
        search_by_gender(1, 0)
        search_by_brand(1)
        search_by_type(1)
        display_results(1, [], "")

    elif tipe == 2:
        if DIAGNOSTICS: print('SHOW: Home Screen')
        hide_previous_screen() # Hide last screen
        SCREEN_MODE = 1 # Set to Mode 2 (Home Screen)
        homeCanvas.place(x = 0, y = 0)

        productTypeSelected.set("Product Type")
        sizeSelected.set("Size")
        colourSelected.set("Colour")
        brandSelected.set("Brand")
        genderSelected.set("Gender")

        for i in range(6):
            [genderMinimumPriceEntry, genderMaximumPriceEntry, brandMinimumPriceEntry, brandMaximumPriceEntry, typeMinimumPriceEntry, typeMaximumPriceEntry][i].delete(0, 'end')

        for i in range(3):
            [genderMinimumPriceEntry, brandMinimumPriceEntry, typeMinimumPriceEntry][i].insert(0, 'Price Min')
            [genderMaximumPriceEntry, brandMaximumPriceEntry, typeMaximumPriceEntry][i].insert(0, 'Price Max')
            
    elif tipe == 3:
        if DIAGNOSTICS: print('HIDE: Home Screen')
        homeCanvas.place_forget()

#----------------------------------------------------

def search_by_gender(tipe, gender):
    global genderCanvas, SCREEN_MODE, redTopFrame, greenTopFrame, orangeTopFrame, productTypeSelected, sizeSelected, colourSelected, brandSelected, genderMinimumPriceEntry, genderMaximumPriceEntry, stylishYouGreen_Label, stylishYouOrange_Label, stylishYouRed_Label, genderSelected


    if tipe == 1:
        if DIAGNOSTICS: print('CREATE: Search by Gender Screen')
        genderCanvas = Canvas(mainWindow, width = RESOLUTION[0], height = RESOLUTION[1], bd = 0, highlightthickness = 0, background = colours[e.ultraWhite])
        redTopFrame = Frame(genderCanvas, bg = colours[e.redStyle], width = 400, height = 100)
        greenTopFrame = Frame(genderCanvas, bg = colours[e.greenStyle], width = 400, height = 100)
        orangeTopFrame = Frame(genderCanvas, bg = colours[e.orangeStyle], width = 400, height = 100)

        # Home Button
        homeButton = Button(genderCanvas, width = 40, height = 2, bd = 0, text = '<< Home', font = ('Arial Black', 8), bg = colours[e.mainStyle], fg = colours[e.ultraWhite], command = lambda: home_menu(2))
        homeButton.place(relx = 0.5, rely = 0.9, anchor = CENTER)

        # Drop Downs
        product_type_drop = OptionMenu(genderCanvas, productTypeSelected, *product_type_options, command = option_changed)
        size_drop = OptionMenu(genderCanvas, sizeSelected, *clothing_size_options, command = option_changed)
        colour_drop = OptionMenu(genderCanvas, colourSelected, *colour_options, command = option_changed)
        brand_drop = OptionMenu(genderCanvas, brandSelected, *brand_options, command = option_changed)

        drop_menus = [product_type_drop, size_drop, colour_drop, brand_drop]

        for i in range(len(drop_menus)):
            drop_menus[i].config(width = 35)
            drop_menus[i].config(relief = FLAT)
            drop_menus[i].config(bg = colours[e.mediumGrey])
            drop_menus[i].config(font=('Arial Black', 10))
            drop_menus[i].config(fg = colours[e.greyText])
            drop_menus[i].config(bd = 0)
            drop_menus[i].config(highlightthickness = 0)
            drop_menus[i].config(indicatoron = 0)
            drop_menus[i].place(relx = 0.5, rely = [0.2, 0.25, 0.3, 0.35][i], anchor = CENTER)

        # Price Entries
        genderMinimumPriceEntry = Entry(genderCanvas, width = 15, bd = 0, font = ('Arial Black', 10), bg = colours[e.mediumGrey], fg = colours[e.greyText], justify = 'center')
        genderMaximumPriceEntry = Entry(genderCanvas, width = 15, bd = 0, font = ('Arial Black', 10), bg = colours[e.mediumGrey], fg = colours[e.greyText], justify = 'center')

        genderMinimumPriceEntry.insert(0, 'Price Min')
        genderMaximumPriceEntry.insert(0, 'Price Max')

        genderMinimumPriceEntry.place(relx = 0.3, rely = 0.4, anchor = CENTER)
        genderMaximumPriceEntry.place(relx = 0.7, rely = 0.4, anchor = CENTER)

        # Load Logo
        stylishYouGreen = Image.open("graphics/StylishYou_Logo_Green.png")
        stylishYouGreen = stylishYouGreen.resize((80, 80))
        stylishYouGreen = ImageTk.PhotoImage(stylishYouGreen)

        stylishYouGreen_Label = Label(greenTopFrame, image=stylishYouGreen, bd = 0)
        stylishYouGreen_Label.image = stylishYouGreen

        # --

        stylishYouOrange = Image.open("graphics/StylishYou_Logo_Orange.png")
        stylishYouOrange = stylishYouOrange.resize((80, 80))
        stylishYouOrange = ImageTk.PhotoImage(stylishYouOrange)

        stylishYouOrange_Label = Label(orangeTopFrame, image=stylishYouOrange, bd = 0)
        stylishYouOrange_Label.image = stylishYouOrange

        # --

        stylishYouRed = Image.open("graphics/StylishYou_Logo_Red.png")
        stylishYouRed = stylishYouRed.resize((80, 80))
        stylishYouRed = ImageTk.PhotoImage(stylishYouRed)

        stylishYouRed_Label = Label(redTopFrame, image=stylishYouRed, bd = 0)
        stylishYouRed_Label.image = stylishYouRed

        # Find Button
        # gender, product_type, size, colour, brand, price_min, price_max
        findButton = Button(genderCanvas, width = 40, height = 2, bd = 0, text = 'Find', font = ('Arial Black', 8), bg = colours[e.mainStyle], fg = colours[e.ultraWhite], command = lambda: results_by_gender(genderSelected.get(), productTypeSelected.get(), sizeSelected.get(), colourSelected.get(), brandSelected.get()))
        findButton.place(relx = 0.5, rely = 0.8, anchor = CENTER)

    elif tipe == 2:
        if DIAGNOSTICS: print('SHOW: Search by Gender Screen (%s)' % (genders[gender]))
        hide_previous_screen() # Hide last screen
        SCREEN_MODE = 2 # Set to Mode 2 (Gender Screen)
        genderCanvas.place(x = 0, y = 0)

        # Determine Top Bar Colour
        for i, idx in enumerate([greenTopFrame, redTopFrame, orangeTopFrame, orangeTopFrame]):
            if i == gender:
                idx.place(relx = 0.5, rely = 0, anchor = N)
                genderSelected.set(genders[i])

        # Determine Top Bar Logo
        for i, idx in enumerate([stylishYouGreen_Label, stylishYouRed_Label, stylishYouOrange_Label, stylishYouOrange_Label]):
            if i == gender:
                idx.place(relx = 0.5, rely = 0.5, anchor = CENTER)



    elif tipe == 3:
        if DIAGNOSTICS: print('HIDE: Search by Gender Screen')
        genderCanvas.place_forget()
        redTopFrame.place_forget()
        greenTopFrame.place_forget()
        orangeTopFrame.place_forget()

#----------------------------------------------------

def search_by_brand(tipe):
    global SCREEN_MODE, brandCanvas, productTypeSelected, sizeSelected, colourSelected, genderSelected, brandMinimumPriceEntry, brandMaximumPriceEntry

    if tipe == 1:
        if DIAGNOSTICS: print('CREATE: Search by Brand Screen')
        brandCanvas = Canvas(mainWindow, width = RESOLUTION[0], height = RESOLUTION[1], bd = 0, highlightthickness = 0, background = colours[e.ultraWhite])

        # Top Bar
        topFrame = Frame(brandCanvas, bg = colours[e.mainStyle], width = 400, height = 100)
        topFrame.place(relx = 0.5, rely = 0, anchor = N)

        # Home Button
        homeButton = Button(brandCanvas, width = 40, height = 2, bd = 0, text = '<< Home', font = ('Arial Black', 8), bg = colours[e.mainStyle], fg = colours[e.ultraWhite], command = lambda: home_menu(2))
        homeButton.place(relx = 0.5, rely = 0.9, anchor = CENTER)

        # Drop Downs
        product_type_drop = OptionMenu(brandCanvas, productTypeSelected, *product_type_options, command = option_changed)
        size_drop = OptionMenu(brandCanvas, sizeSelected, *clothing_size_options, command = option_changed)
        colour_drop = OptionMenu(brandCanvas, colourSelected, *colour_options, command = option_changed)
        gender_drop = OptionMenu(brandCanvas, genderSelected, *gender_options, command = option_changed)

        drop_menus = [product_type_drop, size_drop, colour_drop, gender_drop]

        for i in range(len(drop_menus)):
            drop_menus[i].config(width = 35)
            drop_menus[i].config(relief = FLAT)
            drop_menus[i].config(bg = colours[e.mediumGrey])
            drop_menus[i].config(font=('Arial Black', 10))
            drop_menus[i].config(fg = colours[e.greyText])
            drop_menus[i].config(bd = 0)
            drop_menus[i].config(highlightthickness = 0)
            drop_menus[i].config(indicatoron = 0)
            drop_menus[i].place(relx = 0.5, rely = [0.2, 0.25, 0.3, 0.35][i], anchor = CENTER)

        # Price Entries
        brandMinimumPriceEntry = Entry(brandCanvas, width = 15, bd = 0, font = ('Arial Black', 10), bg = colours[e.mediumGrey], fg = colours[e.greyText], justify = 'center')
        brandMaximumPriceEntry = Entry(brandCanvas, width = 15, bd = 0, font = ('Arial Black', 10), bg = colours[e.mediumGrey], fg = colours[e.greyText], justify = 'center')

        brandMinimumPriceEntry.insert(0, 'Price Min')
        brandMaximumPriceEntry.insert(0, 'Price Max')

        brandMinimumPriceEntry.place(relx = 0.3, rely = 0.4, anchor = CENTER)
        brandMaximumPriceEntry.place(relx = 0.7, rely = 0.4, anchor = CENTER)

        # Load Logo
        stylishYouMain = Image.open("graphics/StylishYou_Logo_Main.png")
        stylishYouMain = stylishYouMain.resize((80, 80))
        stylishYouMain = ImageTk.PhotoImage(stylishYouMain)

        stylishYouMain_Label = Label(topFrame, image=stylishYouMain, bd = 0)
        stylishYouMain_Label.image = stylishYouMain

        stylishYouMain_Label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        # Find Button
        # product_type, size, colour, gender
        findButton = Button(brandCanvas, width = 40, height = 2, bd = 0, text = 'Find', font = ('Arial Black', 8), bg = colours[e.mainStyle], fg = colours[e.ultraWhite], command = lambda: results_by_brand(productTypeSelected.get(), sizeSelected.get(), colourSelected.get(), genderSelected.get()))
        findButton.place(relx = 0.5, rely = 0.8, anchor = CENTER)

    elif tipe == 2:
        if DIAGNOSTICS: print('SHOW: Search by Brand Screen')
        hide_previous_screen() # Hide last screen
        SCREEN_MODE = 3 # Set to Mode 3 (Brand Screen)
        brandCanvas.place(x = 0, y = 0)

    elif tipe == 3:
        if DIAGNOSTICS: print('HIDE: Search by Brand Screen')
        brandCanvas.place_forget()

#----------------------------------------------------

def search_by_type(tipe):
    global SCREEN_MODE, typeCanvas, brandSelected, sizeSelected, colourSelected, genderSelected, typeMinimumPriceEntry, typeMaximumPriceEntry

    if tipe == 1:
        if DIAGNOSTICS: print('CREATE: Search by Product Type Screen')
        typeCanvas = Canvas(mainWindow, width = RESOLUTION[0], height = RESOLUTION[1], bd = 0, highlightthickness = 0, background = colours[e.ultraWhite])

        # Top Bar
        topFrame = Frame(typeCanvas, bg = colours[e.mainStyle], width = 400, height = 100)
        topFrame.place(relx = 0.5, rely = 0, anchor = N)

        # Home Button
        homeButton = Button(typeCanvas, width = 40, height = 2, bd = 0, text = '<< Home', font = ('Arial Black', 8), bg = colours[e.mainStyle], fg = colours[e.ultraWhite], command = lambda: home_menu(2))
        homeButton.place(relx = 0.5, rely = 0.9, anchor = CENTER)

        # Drop Downs
        brand_drop = OptionMenu(typeCanvas, brandSelected, *brand_options, command = option_changed)
        size_drop = OptionMenu(typeCanvas, sizeSelected, *clothing_size_options, command = option_changed)
        colour_drop = OptionMenu(typeCanvas, colourSelected, *colour_options, command = option_changed)
        gender_drop = OptionMenu(typeCanvas, genderSelected, *gender_options, command = option_changed)

        drop_menus = [brand_drop, size_drop, colour_drop, gender_drop]

        for i in range(len(drop_menus)):
            drop_menus[i].config(width = 35)
            drop_menus[i].config(relief = FLAT)
            drop_menus[i].config(bg = colours[e.mediumGrey])
            drop_menus[i].config(font=('Arial Black', 10))
            drop_menus[i].config(fg = colours[e.greyText])
            drop_menus[i].config(bd = 0)
            drop_menus[i].config(highlightthickness = 0)
            drop_menus[i].config(indicatoron = 0)
            drop_menus[i].place(relx = 0.5, rely = [0.2, 0.25, 0.3, 0.35][i], anchor = CENTER)

        # Price Entries
        typeMinimumPriceEntry = Entry(typeCanvas, width = 15, bd = 0, font = ('Arial Black', 10), bg = colours[e.mediumGrey], fg = colours[e.greyText], justify = 'center')
        typeMaximumPriceEntry = Entry(typeCanvas, width = 15, bd = 0, font = ('Arial Black', 10), bg = colours[e.mediumGrey], fg = colours[e.greyText], justify = 'center')

        typeMinimumPriceEntry.insert(0, 'Price Min')
        typeMaximumPriceEntry.insert(0, 'Price Max')

        typeMinimumPriceEntry.place(relx = 0.3, rely = 0.4, anchor = CENTER)
        typeMaximumPriceEntry.place(relx = 0.7, rely = 0.4, anchor = CENTER)

        # Load Logo
        stylishYouMain = Image.open("graphics/StylishYou_Logo_Main.png")
        stylishYouMain = stylishYouMain.resize((80, 80))
        stylishYouMain = ImageTk.PhotoImage(stylishYouMain)

        stylishYouMain_Label = Label(topFrame, image=stylishYouMain, bd = 0)
        stylishYouMain_Label.image = stylishYouMain

        stylishYouMain_Label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        # Find Button
        findButton = Button(typeCanvas, width = 40, height = 2, bd = 0, text = 'Find', font = ('Arial Black', 8), bg = colours[e.mainStyle], fg = colours[e.ultraWhite], command = lambda: results_by_product_type(brandSelected.get(), sizeSelected.get(), colourSelected.get(), genderSelected.get()))
        findButton.place(relx = 0.5, rely = 0.8, anchor = CENTER)

    elif tipe == 2:
        if DIAGNOSTICS: print('SHOW: Search by Product Type Screen')
        hide_previous_screen() # Hide last screen
        SCREEN_MODE = 4 # Set to Mode 4 (Product Type Screen)
        typeCanvas.place(x = 0, y = 0)

    elif tipe == 3:
        if DIAGNOSTICS: print('HIDE: Search by Product Type Screen')
        typeCanvas.place_forget()

#----------------------------------------------------

def display_results(tipe, results, gender):
    global SCREEN_MODE, tableCanvas, resultsCanvas, resultsOrangeTopFrame, resultsRedTopFrame, resultsGreenTopFrame, resultsMainTopFrame, backButton, resultsStylishYouGreen_Label, resultsStylishYouRed_Label, resultsStylishYouOrange_Label, resultsStylishYouMain_Label, e
    if tipe == 1:
        if DIAGNOSTICS: print('CREATE: Results Screen')
        resultsCanvas = Canvas(mainWindow, width = RESOLUTION[0], height = RESOLUTION[1], bd = 0, highlightthickness = 0, background = colours[e.ultraWhite])

        # Home Button
        homeButton = Button(resultsCanvas, width = 40, height = 2, bd = 0, text = 'Home', font = ('Arial Black', 8), bg = colours[e.mainStyle], fg = colours[e.ultraWhite], command = lambda: home_menu(2))
        homeButton.place(relx = 0.5, rely = 0.9, anchor = CENTER)

        # Back Button
        backButton = Button(resultsCanvas, width = 40, height = 2, bd = 0, text = '<< Back', font = ('Arial Black', 8), bg = colours[e.mainStyle], fg = colours[e.ultraWhite])
        backButton.place(relx = 0.5, rely = 0.8, anchor = CENTER)

        # Top Frames
        resultsRedTopFrame = Frame(resultsCanvas, bg = colours[e.redStyle], width = 400, height = 100)
        resultsGreenTopFrame = Frame(resultsCanvas, bg = colours[e.greenStyle], width = 400, height = 100)
        resultsOrangeTopFrame = Frame(resultsCanvas, bg = colours[e.orangeStyle], width = 400, height = 100)
        resultsMainTopFrame = Frame(resultsCanvas, bg = colours[e.mainStyle], width = 400, height = 100)

        # Load Logo
        stylishYouGreen = Image.open("graphics/StylishYou_Logo_Green.png")
        stylishYouGreen = stylishYouGreen.resize((80, 80))
        stylishYouGreen = ImageTk.PhotoImage(stylishYouGreen)

        resultsStylishYouGreen_Label = Label(resultsGreenTopFrame, image=stylishYouGreen, bd = 0)
        resultsStylishYouGreen_Label.image = stylishYouGreen

        # --

        stylishYouOrange = Image.open("graphics/StylishYou_Logo_Orange.png")
        stylishYouOrange = stylishYouOrange.resize((80, 80))
        stylishYouOrange = ImageTk.PhotoImage(stylishYouOrange)

        resultsStylishYouOrange_Label = Label(resultsOrangeTopFrame, image=stylishYouOrange, bd = 0)
        resultsStylishYouOrange_Label.image = stylishYouOrange

        # --

        stylishYouRed = Image.open("graphics/StylishYou_Logo_Red.png")
        stylishYouRed = stylishYouRed.resize((80, 80))
        stylishYouRed = ImageTk.PhotoImage(stylishYouRed)

        resultsStylishYouRed_Label = Label(resultsRedTopFrame, image=stylishYouRed, bd = 0)
        resultsStylishYouRed_Label.image = stylishYouRed

        # --

        stylishYouMain = Image.open("graphics/StylishYou_Logo_Main.png")
        stylishYouMain = stylishYouMain.resize((80, 80))
        stylishYouMain = ImageTk.PhotoImage(stylishYouMain)

        resultsStylishYouMain_Label = Label(resultsMainTopFrame, image=stylishYouMain, bd = 0)
        resultsStylishYouMain_Label.image = stylishYouMain

    elif tipe == 2:
        if DIAGNOSTICS: print('SHOW: Results Screen')
        hide_previous_screen()
        PREVIOUS_SCREEN = SCREEN_MODE

        if PREVIOUS_SCREEN == 2: # Came From Gender
            backButton.config(command = lambda: search_by_gender(2, genders.index(gender)))
        elif PREVIOUS_SCREEN == 3: # Came From Brand
            backButton.config(command = lambda: search_by_brand(2))
        elif PREVIOUS_SCREEN == 4: # Came From Type
            backButton.config(command = lambda: search_by_type(2))

        SCREEN_MODE = 5 # Set to Mode 5 (Results Screen)
        resultsCanvas.place(x = 0, y = 0)

        # Screen Mode | 1 - Home | 2 - Gender | 3 - Brand | 4 - Product Type | 5 - Results |

        if gender != "":
            if gender == "Boys" or gender == "Girls":
                resultsOrangeTopFrame.place(relx = 0.5, rely = 0, anchor = N)
                resultsStylishYouOrange_Label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
            elif gender == "Mens":
                resultsGreenTopFrame.place(relx = 0.5, rely = 0, anchor = N)
                resultsStylishYouGreen_Label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
            elif gender == "Ladies":
                resultsRedTopFrame.place(relx = 0.5, rely = 0, anchor = N)
                resultsStylishYouRed_Label.place(relx = 0.5, rely = 0.5, anchor = CENTER)
        else:
            resultsMainTopFrame.place(relx = 0.5, rely = 0, anchor = N)
            resultsStylishYouMain_Label.place(relx = 0.5, rely = 0.5, anchor = CENTER)

        print('DISPLAY RESULTS:', len(results), results)

        # Create Table
        tableCanvas = Canvas(mainWindow, width = RESOLUTION[0], height = 420, bd = 0, highlightthickness = 0, background = colours[e.ultraWhite])
        tableCanvas.place(x = 0, y = 110)

        if PREVIOUS_SCREEN == 2 or PREVIOUS_SCREEN == 4:
            for c in range(4):
                title = Label(tableCanvas, width = 12, borderwidth = 1, text = ['Description', 'Brand', 'Quantity', 'Store'][c], font = ('Arial Black', 8), bg = colours[e.mediumGrey], fg = colours[e.ultraBlack], anchor = CENTER, relief = "solid")
                title.place(x = 52 + 99 * c, y = 10, anchor = CENTER)

            for r in range(len(results)):
                for entry in range(4):
                    item = Label(tableCanvas, width = 12, borderwidth = 1, text = [results[r][5], results[r][2], results[r][8], results[r][9]][entry], font = ('Arial Black', 8), bg = colours[e.lightGrey], fg = colours[e.ultraBlack], anchor = CENTER, relief = "solid")
                    item.place(x = 52 + 99 * entry, y = 27.5 + 18 * r, anchor = CENTER)

        elif PREVIOUS_SCREEN == 3:
            for c in range(3):
                title = Label(tableCanvas, width = 15, borderwidth = 1, text = ['Description', 'Quantity', 'Store'][c], font = ('Arial Black', 8), bg = colours[e.mediumGrey], fg = colours[e.ultraBlack], anchor = CENTER, relief = "solid")
                title.place(x = 77.5 + 123 * c, y = 10, anchor = CENTER)

            for r in range(len(results)):
                for entry in range(3):
                    item = Label(tableCanvas, width = 15, borderwidth = 1, text = [results[r][5], results[r][8], results[r][9]][entry], font = ('Arial Black', 8), bg = colours[e.lightGrey], fg = colours[e.ultraBlack], anchor = CENTER, relief = "solid")
                    item.place(x = 77.5 + 123 * entry, y = 27.5 + 18 * r, anchor = CENTER)

    elif tipe == 3:
        if DIAGNOSTICS: print('HIDE: Results Screen')
        resultsCanvas.place_forget()
        resultsRedTopFrame.place_forget()
        resultsGreenTopFrame.place_forget()
        resultsOrangeTopFrame.place_forget()
        resultsMainTopFrame.place_forget()
        tableCanvas.place_forget()

#----------------------------------------------------

def hide_previous_screen():
    if SCREEN_MODE == 1:
        home_menu(3)
    elif SCREEN_MODE == 2:
        search_by_gender(3, 0)
    elif SCREEN_MODE == 3:
        search_by_brand(3)
    elif SCREEN_MODE == 4:
        search_by_type(3)
    elif SCREEN_MODE == 5:
        display_results(3, [], "")

#----------------------------------------------------

########################################################
# Routines                                             #
########################################################

#----------------------------------------------------

def results_by_gender(gender, product_type, size, colour, brand):
    price_min = genderMinimumPriceEntry.get()
    price_max = genderMaximumPriceEntry.get()
    if DIAGNOSTICS: print('SEARCH: Searching by gender using: %s, %s, %s, %s, %s' % (gender, product_type, size, colour, brand))
    final_results = []

    connectionObject = sqlite3.connect('OurProductsDatabase.db')
    cursorObject = connectionObject.cursor()

    search_command = ('SELECT * FROM OurProducts WHERE "Gender" = "%s"' % (gender))

    if product_type != 'Product Type': search_command = search_command + ('AND "Product Type" = "%s"' % (product_type))
        
    if colour != 'Colour': search_command = search_command + ('AND "Colour" = "%s"' % (colour))

    if brand != 'Brand': search_command = search_command + ('AND "Brands" = "%s"' % (brand))

    cursorObject.execute(search_command)
    results = cursorObject.fetchall()

    if size != 'Size':
        for i in range(len(results)):
            
            if results[i][6]:
                count = 0
                sizes = results[i][6].split('/')
                for d in range(len(sizes)):
                    if sizes[d] == size:
                        final_results.append(results[i])
                    else:
                        count = count + 1
                        print(count)
                        print(len(sizes))
                        if count == len(sizes):
                            pass

    if len(final_results) > 0:
        results = final_results
        final_results = []
    
    for i in range(len(results)):
        count = 0
        if results[i][7]: # If a price is in the database for the item
            if price_min != 'Price Min' and price_max != 'Price Max':
                print('Entered for both')
                if results[i][7] >= float(price_min) and results[i][7] <= float(price_max):
                    final_results.append(results[i])

            elif price_min != 'Price Min':
                print('Entered for just min')
                if results[i][7] >= float(price_min):
                    final_results.append(results[i])
            
            elif price_max != 'Price Max':
                print('Entered for just max')
                if results[i][7] <= float(price_max):
                    final_results.append(results[i])
            
            else:
                final_results.append(results[i])

    results = final_results
    final_results = []

    connectionObject.close()

    #print(len(results))
    #print(results)

    display_results(2, results, gender)


#----------------------------------------------------

def results_by_brand(product_type, size, colour, gender):
    connectives = False
    final_results = []
    price_min = brandMinimumPriceEntry.get()
    price_max = brandMaximumPriceEntry.get()
    if DIAGNOSTICS: print('SEARCH: Searching by gender using: %s, %s, %s, %s, %s, %s' % (product_type, size, colour, gender, price_min, price_max))
    
    connectionObject = sqlite3.connect('OurProductsDatabase.db')
    cursorObject = connectionObject.cursor()

    search_command = ('SELECT * FROM OurProducts ')

    if product_type != 'Product Type': 
        search_command = search_command + ('WHERE "Product Type" = "%s"' % (product_type))
        connectives = True
        
    if colour != 'Colour':
        if connectives == True:
            search_command = search_command + ('AND "Colour" = "%s"' % (colour))
        else:
            search_command = search_command + ('WHERE "Colour" = "%s"' % (colour))
            connectives = True

    if gender != 'Gender':
        if connectives == True:
            search_command = search_command + ('AND "Gender" = "%s"' % (gender))
        else:
            search_command = search_command + ('WHERE "Gender" = "%s"' % (gender))
            connectives = True

    cursorObject.execute(search_command)
    results = cursorObject.fetchall()

    if size != 'Size':
        for i in range(len(results)):
            count = 0
            if results[i][6]:
                
                sizes = results[i][6].split('/')
                for d in range(len(sizes)):
                    if sizes[d] == size:
                        final_results.append(results[i])
                    else:
                        count = count + 1
                        if count == len(sizes):
                            pass

    if len(final_results) > 0:
        results = final_results
        final_results = []

    for i in range(len(results)):
        count = 0
        if results[i][7]: # If a price is in the database for the item
            if price_min != 'Price Min' and price_max != 'Price Max':
                print('Entered for both')
                if results[i][7] >= float(price_min) and results[i][7] <= float(price_max):
                    final_results.append(results[i])

            elif price_min != 'Price Min':
                print('Entered for just min')
                if results[i][7] >= float(price_min):
                    final_results.append(results[i])
            
            elif price_max != 'Price Max':
                print('Entered for just max')
                if results[i][7] <= float(price_max):
                    final_results.append(results[i])
            
            else:
                final_results.append(results[i])

    results = final_results
    final_results = []

    connectionObject.close()
    #print('\n', results)
    #print(len(results))

    display_results(2, results, "")

#----------------------------------------------------

def results_by_product_type(brand, size, colour, gender):
    connectives = False
    final_results = []
    price_min = typeMinimumPriceEntry.get()
    price_max = typeMaximumPriceEntry.get()
    if DIAGNOSTICS: print('SEARCH: Searching by gender using: %s, %s, %s, %s, %s, %s' % (brand, size, colour, gender, price_min, price_max))

    connectionObject = sqlite3.connect('OurProductsDatabase.db')
    cursorObject = connectionObject.cursor()

    search_command = ('SELECT * FROM OurProducts ')

    if brand != 'Brand': 
        search_command = search_command + ('WHERE "Brands" = "%s"' % (brand))
        connectives = True
        
    if colour != 'Colour':
        if connectives == True:
            search_command = search_command + ('AND "Colour" = "%s"' % (colour))
        else:
            search_command = search_command + ('WHERE "Colour" = "%s"' % (colour))
            connectives = True

    if gender != 'Gender':
        if connectives == True:
            search_command = search_command + ('AND "Gender" = "%s"' % (gender))
        else:
            search_command = search_command + ('WHERE "Gender" = "%s"' % (gender))
            connectives = True

    cursorObject.execute(search_command)
    results = cursorObject.fetchall()

    if size != 'Size':
        for i in range(len(results)):
            count = 0
            if results[i][6]:
                
                sizes = results[i][6].split('/')
                for d in range(len(sizes)):
                    if sizes[d] == size:
                        final_results.append(results[i])
                    else:
                        count = count + 1
                        if count == len(sizes):
                            pass

    if len(final_results) > 0:
        results = final_results
        final_results = []

    for i in range(len(results)):
        count = 0
        if results[i][7]: # If a price is in the database for the item
            if price_min != 'Price Min' and price_max != 'Price Max':
                print('Entered for both')
                if results[i][7] >= float(price_min) and results[i][7] <= float(price_max):
                    final_results.append(results[i])

            elif price_min != 'Price Min':
                print('Entered for just min')
                if results[i][7] >= float(price_min):
                    final_results.append(results[i])
            
            elif price_max != 'Price Max':
                print('Entered for just max')
                if results[i][7] <= float(price_max):
                    final_results.append(results[i])
            
            else:
                final_results.append(results[i])

    results = final_results
    final_results = []

    connectionObject.close()
    #print('\n', results)
    #print(len(results))

    display_results(2, results, "")

#----------------------------------------------------

def option_changed(arg):
    pass
    #if arg == "Shoes":
        #print('Shoes')
        

#----------------------------------------------------

########################################################
# Run App                                              #
########################################################

setup_tk()
mainWindow.mainloop()