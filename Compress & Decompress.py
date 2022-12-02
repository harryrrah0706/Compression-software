import os
import shutil
import time
import sys
import zipfile
from tkinter import *


# Function that places the first Label frame to enable user select between compress and decompress.
def SetCompOrDecompFrame():
    CompOrDecompFrame.place(x=18, y=85)


# Sets the CompOrDecomp StringVar to COMPRESS.
def SetComp():
    CompOrDecomp.set('COMPRESS')
    SetFolderOrFileFrame()


# Sets the CompOrDecomp StringVar to DECOMPRESS.
def SetDecomp():
    CompOrDecomp.set('DECOMPRESS')
    SetDecompressEntryFrame()


# Sets up the FileOrFolder frame which enables choose between compression of folders of files.
def SetFolderOrFileFrame():
    CompOrDecompFrame.destroy()
    FolderOrFileFrame.place(x=18, y=85)
    CompOrDecompState = Label(FolderOrFileFrame, text='SELECTED CHOICE: ' + CompOrDecomp.get(), font='OCRAStd 7', bg='lightblue')
    CompOrDecompState.place(x=0, y=169)


# Sets the FolderOrFile StringVar to FILE
def SetFile():
    FolderOrFile.set('FILE')
    SetCompressFileEntryFrame()


# Sets the FolderOrFile StringVar to FOLDER
def SetFolder():
    FolderOrFile.set('FOLDER')
    SetCompressFolderEntryFrame()


# adds the label that displays selected choice and add the Individual or together selection to the label.
def SetCompressFileIndividual():
    IndividualOrTogether.set('INDIVIDUAL')
    IndividualOrTogetherState = Label(CompressFileEntryFrame, text='SELECTED CHOICE: ' + CompOrDecomp.get() + ' -> ' + FolderOrFile.get() + ' -> ' + IndividualOrTogether.get(), font='OCRAStd 7', bg='lightblue')
    IndividualOrTogetherState.place(x=0, y=169)
    CompressFileDestroyIndividualTogetherObject()


# adds the label that displays selected choice and add the Individual or together selection to the label.
def SetCompressFileTogether():
    IndividualOrTogether.set('TOGETHER')
    IndividualOrTogetherState = Label(CompressFileEntryFrame, text='SELECTED CHOICE: ' + CompOrDecomp.get() + ' -> ' + FolderOrFile.get() + ' -> ' + IndividualOrTogether.get(), font='OCRAStd 7', bg='lightblue')
    IndividualOrTogetherState.place(x=0, y=169)
    CompressFileDestroyIndividualTogetherObject()


# adds the label that displays selected choice and add the Individual or together selection to the label.
def SetCompressFolderIndividual():
    IndividualOrTogether.set('INDIVIDUAL')
    IndividualOrTogetherState = Label(CompressFolderEntryFrame, text='SELECTED CHOICE: ' + CompOrDecomp.get() + ' -> ' + FolderOrFile.get() + ' -> ' + IndividualOrTogether.get(), font='OCRAStd 7', bg='lightblue')
    IndividualOrTogetherState.place(x=0, y=169)
    CompressFolderDestroyIndividualTogetherObject()


# adds the label that displays selected choice and add the Individual or together selection to the label.
def SetCompressFolderTogether():
    IndividualOrTogether.set('TOGETHER')
    IndividualOrTogetherState = Label(CompressFolderEntryFrame, text='SELECTED CHOICE: ' + CompOrDecomp.get() + ' -> ' + FolderOrFile.get() + ' -> ' + IndividualOrTogether.get(), font='OCRAStd 7', bg='lightblue')
    IndividualOrTogetherState.place(x=0, y=169)
    CompressFolderDestroyIndividualTogetherObject()


# Destroy previous frame while displaying the new File entry frame, and adds the label that displays selected choice.
def SetCompressFileEntryFrame():
    FolderOrFileFrame.destroy()
    CompressFileEntryFrame.place(x=18, y=85)
    FolderOrFileState = Label(CompressFileEntryFrame, text='SELECTED CHOICE: ' + CompOrDecomp.get() + ' -> ' + FolderOrFile.get(), font='OCRAStd 7', bg='lightblue')
    FolderOrFileState.place(x=0, y=169)


# Destroy previous frame while displaying the new Folder entry frame, and adds the label that displays selected choice.
def SetCompressFolderEntryFrame():
    FolderOrFileFrame.destroy()
    CompressFolderEntryFrame.place(x=18, y=85)
    FolderOrFileState = Label(CompressFolderEntryFrame, text='SELECTED CHOICE: ' + CompOrDecomp.get() + ' -> ' + FolderOrFile.get(), font='OCRAStd 7', bg='lightblue')
    FolderOrFileState.place(x=0, y=169)


# Destroy previous frame while displaying the new Decompress entry frame, and adds the label that displays selected choice.
def SetDecompressEntryFrame():
    CompOrDecompFrame.destroy()
    DecompressEntryFrame.place(x=18, y=85)
    CompOrDecompState = Label(DecompressEntryFrame, text='SELECTED CHOICE: ' + CompOrDecomp.get(), font='OCRAStd 7', bg='lightblue')
    CompOrDecompState.place(x=0, y=169)


# Unbinds all keys and bind another double click key with the final frame for Decompression.
def SetDecompressInformationFrames():
    DecompressEntryFrame.destroy()
    FirstConfirmLabel.destroy()
    SecondConfirmLabel.destroy()
    MainWindow.geometry('780x315+450+200')
    WelcomeMessage.place(x=240, y=8)
    DecompressWaitListListboxFrame.destroy()
    DecompressSearchResultListboxFrame.destroy()
    MainWindow.unbind('<Delete>')
    MainWindow.unbind('<Enter>')
    MainWindow.unbind('<Double-1>')
    DecompressInformationFrame.place(x=398, y=85)
    DecompressIndividualListboxFrame.place(x=18, y=85)
    MainWindow.bind('<Double-Button-1>', SetDecompressInformationFrame)


# Unbinds all keys and bind another double click key with the final frame for Compress-File-Individual.
def SetCompressFolderIndividualFrames():
    CompressFolderEntryFrame.destroy()
    SecondConfirmLabel.destroy()
    FirstConfirmLabel.destroy()
    MainWindow.geometry('780x315+450+200')
    WelcomeMessage.place(x=240, y=8)
    CompressFolderWaitListListboxFrame.destroy()
    CompressFolderSearchResultListboxFrame.destroy()
    MainWindow.unbind('<Delete>')
    MainWindow.unbind('<Enter>')
    MainWindow.unbind('<Double-1>')
    CompressFolderIndividualListboxFrame.place(x=18, y=85)
    CompressFolderInformationFrame.place(x=398, y=85)
    MainWindow.bind('<Double-Button-1>', SetCompressFolderIndividualInformationFrame)


# Unbinds all keys and bind another double click key with the final frame for Compress-Folder-Individual.
def SetCompressFileIndividualFrames():
    CompressFileEntryFrame.destroy()
    SecondConfirmLabel.destroy()
    FirstConfirmLabel.destroy()
    WelcomeMessage.place(x=240, y=8)
    MainWindow.geometry('780x315+450+200')
    CompressFileWaitListListboxFrame.destroy()
    CompressFileSearchResultListboxFrame.destroy()
    MainWindow.unbind('<Delete>')
    MainWindow.unbind('<Enter>')
    MainWindow.unbind('<Double-1>')
    CompressFileIndividualListboxFrame.place(x=18, y=85)
    CompressFileInformationFrame.place(x=398, y=85)
    MainWindow.bind('<Double-Button-1>', SetCompressFileIndividualInformationFrame)


# Unbinds all keys displays the information frame.
def SetCompressFolderTogetherFrames():
    CompressFolderEntryFrame.destroy()
    SecondConfirmLabel.destroy()
    FirstConfirmLabel.destroy()
    MainWindow.geometry('780x315+450+200')
    WelcomeMessage.place(x=240, y=8)
    CompressFolderWaitListListboxFrame.destroy()
    CompressFolderSearchResultListboxFrame.destroy()
    MainWindow.unbind('<Delete>')
    MainWindow.unbind('<Enter>')
    MainWindow.unbind('<Double-1>')
    CompressFolderInformationFrame.place(x=398, y=85)
    CompressFolderZipNameEntryFrame.place(x=18, y=85)


# Unbinds all keys displays the information frame.
def SetCompressFileTogetherFrames():
    CompressFileEntryFrame.destroy()
    SecondConfirmLabel.destroy()
    FirstConfirmLabel.destroy()
    MainWindow.geometry('780x315+450+200')
    WelcomeMessage.place(x=240, y=8)
    CompressFileWaitListListboxFrame.destroy()
    CompressFileSearchResultListboxFrame.destroy()
    MainWindow.unbind('<Delete>')
    MainWindow.unbind('<Enter>')
    MainWindow.unbind('<Double-1>')
    CompressFileInformationFrame.place(x=398, y=85)
    CompressFileZipNameEntryFrame.place(x=18, y=85)


# Sets up the information frame that outputs the statistics of Compress-File-Individual.
def SetCompressFileIndividualInformationFrame(x):
    if len(CompressFileFileNameListbox.curselection()) == 0:
        None
    else:
        Position = CompressFileFileNameListbox.curselection()[0]
        ClearLabel = Label(CompressFileInformationFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=3)
        CompressionTimeLabel = Label(CompressFileInformationFrame, text='>>> TIME TAKEN: ' + InfoList[Position][0] + ' seconds', font='OCRAStd 8', bg='lightblue')
        CompressionTimeLabel.place(x=0, y=3)
        ClearLabel = Label(CompressFileInformationFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=23)
        OriginalFileSizeLabel = Label(CompressFileInformationFrame, text='>>> ORIGINAL FILE SIZE: ' + str(int(InfoList[Position][1])) + ' KB', font='OCRAStd 8', bg='lightblue')
        OriginalFileSizeLabel.place(x=0, y=23)
        ClearLabel = Label(CompressFileInformationFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=43)
        CompressedFileSizeLabel = Label(CompressFileInformationFrame, text='>>> COMPRESSED FILE SIZE: ' + str(int(InfoList[Position][2])) + ' KB', font='OCRAStd 8', bg='lightblue')
        CompressedFileSizeLabel.place(x=0, y=43)
        ClearLabel = Label(CompressFileInformationFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=63)
        ReducedSizeLabel = Label(CompressFileInformationFrame, text='>>> REDUCED PERCENTAGE SIZE: ' + InfoList[Position][3], font='OCRAStd 8', bg='lightblue')
        ReducedSizeLabel.place(x=0, y=63)
        ClearLabel = Label(CompressFileInformationFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=83)
        CompressedFileDirectoryLabel1 = Label(CompressFileInformationFrame, text='>>> DIRECTORY OF COMPRESSED FILE:', font='OCRAStd 8', bg='lightblue')
        CompressedFileDirectoryLabel1.place(x=0, y=83)
        ClearLabel = Label(CompressFileInformationFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=100)
        CompressedFileDirectoryLabel2 = Label(CompressFileInformationFrame, text=InfoList[Position][4], font='OCRAStd 8', bg='lightblue')
        CompressedFileDirectoryLabel2.place(x=15, y=100)
        CompressFileShowInFolderButton.place(x=105, y=160)


# Sets up the information frame that outputs the statistics of Compress-File-Together.
def SetCompressFileTogetherInformationFrame(CompressRatio, CompressedFileSize, TotalOriginalSize, TotalTime):
    CompressionTimeLabel = Label(CompressFileInformationFrame, text='>>> TIME TAKEN: ' + str(TotalTime) + ' seconds', font='OCRAStd 8', bg='lightblue')
    CompressionTimeLabel.place(x=0, y=3)
    OriginalFileSizeLabel = Label(CompressFileInformationFrame, text='>>> ORIGINAL FILE SIZE: ' + str(int(TotalOriginalSize)) + ' KB', font='OCRAStd 8', bg='lightblue')
    OriginalFileSizeLabel.place(x=0, y=23)
    CompressedFileSizeLabel = Label(CompressFileInformationFrame, text='>>> COMPRESSED FILE SIZE: ' + str(int(CompressedFileSize)) + ' KB', font='OCRAStd 8', bg='lightblue')
    CompressedFileSizeLabel.place(x=0, y=43)
    ReducedSizeLabel = Label(CompressFileInformationFrame, text='>>> REDUCED PERCENTAGE SIZE: ' + CompressRatio, font='OCRAStd 8', bg='lightblue')
    ReducedSizeLabel.place(x=0, y=63)
    CompressedFileDirectoryLabel1 = Label(CompressFileInformationFrame, text='>>> DIRECTORY OF COMPRESSED FILE:', font='OCRAStd 8', bg='lightblue')
    CompressedFileDirectoryLabel1.place(x=0, y=83)
    CompressedFileDirectoryLabel2 = Label(CompressFileInformationFrame, text=EditCompressFileDirectory(ZipName.get()), font='OCRAStd 8', bg='lightblue')
    CompressedFileDirectoryLabel2.place(x=15, y=100)
    CompressFileShowInFolderButton.place(x=105, y=160)


# Sets up the information frame that outputs the statistics of Compress-Folder-Individual.
def SetCompressFolderIndividualInformationFrame(x):
    if len(CompressFolderFileNameListbox.curselection()) == 0:
        None
    else:
        Position = CompressFolderFileNameListbox.curselection()[0]
        ClearLabel = Label(CompressFolderInformationFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=3)
        CompressionTimeLabel = Label(CompressFolderInformationFrame, text='>>> TIME TAKEN: ' + InfoList[Position][0] + ' seconds', font='OCRAStd 8', bg='lightblue')
        CompressionTimeLabel.place(x=0, y=3)
        ClearLabel = Label(CompressFolderInformationFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=23)
        OriginalFolderSizeLabel = Label(CompressFolderInformationFrame, text='>>> ORIGINAL FILE SIZE: ' + str(int(InfoList[Position][1])) + ' KB', font='OCRAStd 8', bg='lightblue')
        OriginalFolderSizeLabel.place(x=0, y=23)
        ClearLabel = Label(CompressFolderInformationFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=43)
        CompressedFolderSizeLabel = Label(CompressFolderInformationFrame, text='>>> COMPRESSED FILE SIZE: ' + str(int(InfoList[Position][2])) + ' KB', font='OCRAStd 8', bg='lightblue')
        CompressedFolderSizeLabel.place(x=0, y=43)
        ClearLabel = Label(CompressFolderInformationFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=63)
        ReducedSizeLabel = Label(CompressFolderInformationFrame, text='>>> REDUCED PERCENTAGE SIZE: ' + InfoList[Position][3], font='OCRAStd 8', bg='lightblue')
        ReducedSizeLabel.place(x=0, y=63)
        ClearLabel = Label(CompressFolderInformationFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=83)
        CompressedFolderDirectoryLabel1 = Label(CompressFolderInformationFrame, text='>>> DIRECTORY OF COMPRESSED FILE:', font='OCRAStd 8', bg='lightblue')
        CompressedFolderDirectoryLabel1.place(x=0, y=83)
        ClearLabel = Label(CompressFolderInformationFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=100)
        CompressedFolderDirectoryLabel2 = Label(CompressFolderInformationFrame, text=InfoList[Position][4], font='OCRAStd 8', bg='lightblue')
        CompressedFolderDirectoryLabel2.place(x=15, y=100)
        CompressFolderShowInFolderButton.place(x=105, y=160)


# Sets up the information frame that outputs the statistics of Compress-Folder-Together.
def SetCompressFolderTogetherInformationFrame(CompressRatio, CompressedFileSize, TotalOriginalFileSize, CompressionTime):
    CompressionTimeLabel = Label(CompressFolderInformationFrame, text='>>> TIME TAKEN: ' + str(CompressionTime) + ' seconds', font='OCRAStd 8', bg='lightblue')
    CompressionTimeLabel.place(x=0, y=3)
    OriginalFileSizeLabel = Label(CompressFolderInformationFrame, text='>>> ORIGINAL FILE SIZE: ' + str(int(TotalOriginalFileSize)) + ' KB', font='OCRAStd 8', bg='lightblue')
    OriginalFileSizeLabel.place(x=0, y=23)
    CompressedFileSizeLabel = Label(CompressFolderInformationFrame, text='>>> COMPRESSED FILE SIZE: ' + str(int(CompressedFileSize)) + ' KB', font='OCRAStd 8', bg='lightblue')
    CompressedFileSizeLabel.place(x=0, y=43)
    ReducedSizeLabel = Label(CompressFolderInformationFrame, text='>>> REDUCED PERCENTAGE SIZE: ' + CompressRatio, font='OCRAStd 8', bg='lightblue')
    ReducedSizeLabel.place(x=0, y=63)
    CompressedFileDirectoryLabel1 = Label(CompressFolderInformationFrame, text='>>> DIRECTORY OF COMPRESSED FILE:', font='OCRAStd 8', bg='lightblue')
    CompressedFileDirectoryLabel1.place(x=0, y=83)
    CompressedFileDirectoryLabel2 = Label(CompressFolderInformationFrame, text=EditCompressFileDirectory(ZipName.get()), font='OCRAStd 8', bg='lightblue')
    CompressedFileDirectoryLabel2.place(x=15, y=100)
    CompressFolderShowInFolderButton.place(x=105, y=160)


# Sets up the information frame that outputs the statistics of Decompression.
def SetDecompressInformationFrame(x):
    DecompressIndividualListboxFrame.place()
    if len(DecompressFileNameListbox.curselection()) == 0:
        None
    else:
        Position = DecompressFileNameListbox.curselection()[0]
        ClearLabel = Label(DecompressInformationFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=3)
        CompressionTimeLabel = Label(DecompressInformationFrame, text='>>> TIME TAKEN: ' + str(InfoList[Position][0]) + ' seconds', font='OCRAStd 8', bg='lightblue')
        CompressionTimeLabel.place(x=0, y=3)
        ClearLabel = Label(DecompressInformationFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=23)
        DecompressDirectoryLabel1 = Label(DecompressInformationFrame, text='>>> DIRECTORY OF COMPRESSED FILE:', font='OCRAStd 8', bg='lightblue')
        DecompressDirectoryLabel1.place(x=0, y=23)
        ClearLabel = Label(DecompressInformationFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=40)
        DecompressDirectoryLabel2 = Label(DecompressInformationFrame, text=InfoList[Position][1], font='OCRAStd 8', bg='lightblue')
        DecompressDirectoryLabel2.place(x=15, y=40)
        DecompressShowInFolderButton.place(x=105, y=160)


# Sets the Compress File search result listbox frame and wait list listbox frame.
def SetCompressFileListboxFrames(FileSearchDirectoryList):
    MainWindow.geometry('760x315+450+200')
    try:
        IndividualOrTogetherLabel.place(x=395, y=260)
        CompressFileHintMessage.place(x=0, y=0)
        CompressFileIndividualButton.place(x=641, y=257)
        CompressFileTogetherButton.place(x=641, y=282)
    except TclError:
        None
    CompressFileWaitListListboxFrame.place(x=395, y=135)
    CompressFileSearchResultListboxFrame.place(x=395, y=10)
    EntryFileName = EditEntryFileName()
    CompressFileEntryFrame.configure(text=str(len(FileSearchDirectoryList)) + ' files named "' + EntryFileName + '" are found\nDOUBLE CLICK the file to be waitlisted', fg='green')
    CompressFileSearchResultListbox.delete(0, END)
    CompressFileEntry.delete(first=0, last=len(FileName.get()))
    MainWindow.bind('<Delete>', CompressFileRemoveFromWaitList)
    for file in FileSearchDirectoryList:
        CompressFileSearchResultListbox.insert(END, file)
    MainWindow.bind('<Double-Button-1>', CompressFileAddToWaitList)


# Sets the Compress Folder search result listbox frame and wait list listbox frame.
def SetCompressFolderListboxFrames(FolderSearchDirectoryList):
    MainWindow.geometry('760x315+450+200')
    try:
        IndividualOrTogetherLabel.place(x=395, y=260)
        CompressFolderHintMessage.place(x=0, y=0)
        CompressFolderIndividualButton.place(x=641, y=257)
        CompressFolderTogetherButton.place(x=641, y=282)
    except TclError:
        None
    CompressFolderWaitListListboxFrame.place(x=395, y=135)
    CompressFolderSearchResultListboxFrame.place(x=395, y=10)
    EntryFolderName = EditEntryFileName()
    CompressFolderEntryFrame.configure(text=str(len(FolderSearchDirectoryList)) + ' folders named "' + EntryFolderName + '" are found\nDOUBLE CLICK the file to be waitlisted', fg='green')
    CompressFolderSearchResultListbox.delete(0, END)
    CompressFolderEntry.delete(first=0, last=len(FolderName.get()))
    MainWindow.bind('<Delete>', CompressFolderRemoveFromWaitList)
    for folder in FolderSearchDirectoryList:
        CompressFolderSearchResultListbox.insert(END, folder)
    MainWindow.bind('<Double-Button-1>', CompressFolderAddToWaitList)


# Sets the decompression search result listbox frame and wait list listbox frame.
def SetDecompressListboxFrames(ZipFileSearchDirectoryList):
    MainWindow.geometry('760x315+450+200')
    try:
        DecompressHintMessage.place(x=0, y=0)
    except TclError:
        None
    DecompressWaitListListboxFrame.place(x=395, y=135)
    DecompressSearchResultListboxFrame.place(x=395, y=10)
    EntryZipFileName = EditEntryFileName()
    DecompressEntryFrame.configure(text=str(len(ZipFileSearchDirectoryList)) + ' files named "' + EntryZipFileName + '" are found\nDOUBLE CLICK the file to be waitlisted', fg='green')
    DecompressSearchResultListbox.delete(0, END)
    DecompressEntry.delete(first=0, last=len(ZipFileName.get()))
    MainWindow.bind('<Delete>', DecompressRemoveFromWaitList)
    for zipfilename in ZipFileSearchDirectoryList:
        DecompressSearchResultListbox.insert(END, zipfilename)
    MainWindow.bind('<Double-Button-1>', DecompressAddToWaitList)
    FirstConfirmLabel.place(x=437, y=265)
    MainWindow.bind('<Return>', Decompress)


# Function responsible for adding elements to wait list listbox in Decompression.
def DecompressAddToWaitList(x):
    if len(DecompressSearchResultListbox.curselection()) != 0:
        Name = EditDecompressAddToWaitListName()
        ZipFileToBeAdded = DecompressSearchResultListbox.get((DecompressSearchResultListbox.curselection()))
        if Name not in ClickedList:
            ClearLabel = Label(DecompressEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
            ClearLabel.place(x=0, y=35)
            AddedSuccessfullyLabel = Label(DecompressEntryFrame, text='**SUCCESSFULLY ADDED TO WAIT LIST**', font='OCRAStd 8', bg='lightblue', fg='green')
            AddedSuccessfullyLabel.place(x=40, y=35)
            DecompressWaitListListbox.insert(END, ZipFileToBeAdded)
            ClickedList.append(Name)
        else:
            ClearLabel = Label(DecompressEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
            ClearLabel.place(x=0, y=35)
            AlreadyExistLabel = Label(DecompressEntryFrame, text='**SIMILAR FILE ALREADY EXISTS IN WAIT LIST**', font='OCRAStd 8', bg='lightblue', fg='red')
            AlreadyExistLabel.place(x=5, y=35)
    else:
        ClearLabel = Label(DecompressEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=35)
        SelectFolderLabel = Label(DecompressEntryFrame, text='**NO FILE SELECTED IN LISTBOX**', font='OCRAStd 8', bg='lightblue', fg='red')
        SelectFolderLabel.place(x=55, y=35)


# Function responsible for adding elements to wait list listbox in Compress Folder.
def CompressFolderAddToWaitList(x):
    if len(CompressFolderSearchResultListbox.curselection()) != 0:
        Name = EditCompressFolderAddToWaitListName()
        FolderToBeAdded = CompressFolderSearchResultListbox.get((CompressFolderSearchResultListbox.curselection()))
        if Name not in ClickedList:
            ClearLabel = Label(CompressFolderEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
            ClearLabel.place(x=0, y=35)
            AddedSuccessfullyLabel = Label(CompressFolderEntryFrame, text='**SUCCESSFULLY ADDED TO WAIT LIST**', font='OCRAStd 8', bg='lightblue', fg='green')
            AddedSuccessfullyLabel.place(x=40, y=35)
            CompressFolderWaitListListbox.insert(END, FolderToBeAdded)
            ClickedList.append(Name)
        else:
            ClearLabel = Label(CompressFolderEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
            ClearLabel.place(x=0, y=35)
            AlreadyExistLabel = Label(CompressFolderEntryFrame, text='**SIMILAR FILE ALREADY EXISTS IN WAIT LIST**', font='OCRAStd 8', bg='lightblue', fg='red')
            AlreadyExistLabel.place(x=5, y=35)
    else:
        ClearLabel = Label(CompressFolderEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=35)
        SelectFolderLabel = Label(CompressFolderEntryFrame, text='**NO FILE SELECTED IN LISTBOX**', font='OCRAStd 8', bg='lightblue', fg='red')
        SelectFolderLabel.place(x=55, y=35)


# Function responsible for adding elements to wait list listbox in Compress File.
def CompressFileAddToWaitList(x):
    if len(CompressFileSearchResultListbox.curselection()) != 0:
        Name = EditCompressFileAddToWaitListName()
        FileToBeAdded = CompressFileSearchResultListbox.get(CompressFileSearchResultListbox.curselection())
        if Name not in ClickedList:
            ClearLabel = Label(CompressFileEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
            ClearLabel.place(x=0, y=35)
            AddedSuccessfullyLabel = Label(CompressFileEntryFrame, text='**SUCCESSFULLY ADDED TO WAIT LIST**', font='OCRAStd 8', bg='lightblue', fg='green')
            AddedSuccessfullyLabel.place(x=40, y=35)
            CompressFileWaitListListbox.insert(END, FileToBeAdded)
            ClickedList.append(Name)
        else:
            ClearLabel = Label(CompressFileEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
            ClearLabel.place(x=0, y=35)
            AlreadyExistLabel = Label(CompressFileEntryFrame, text='**SIMILAR FILE ALREADY EXISTS IN WAIT LIST**', font='OCRAStd 8', bg='lightblue', fg='red')
            AlreadyExistLabel.place(x=5, y=35)
    else:
        ClearLabel = Label(CompressFileEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=35)
        SelectFileLabel = Label(CompressFileEntryFrame, text='**NO FILE SELECTED IN LISTBOX**', font='OCRAStd 8', bg='lightblue', fg='red')
        SelectFileLabel.place(x=55, y=35)


# Function responsible for removing elements from wait list listbox in Decompress
def DecompressRemoveFromWaitList(x):
    DecompressHintMessage.destroy()
    if len(DecompressWaitListListbox.curselection()) != 0:
        NameList = EditDecompressDeleteNameList()
        for item in NameList:
            ClickedList.remove(item)
            DecompressWaitListListbox.delete(DecompressWaitListListbox.curselection()[0])
            ClearLabel = Label(DecompressEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
            ClearLabel.place(x=0, y=35)
            DeleteSuccessfullyLabel = Label(DecompressEntryFrame, text='**SUCCESSFULLY DELETED FROM WAIT LIST**', font='OCRAStd 8', bg='lightblue', fg='green')
            DeleteSuccessfullyLabel.place(x=27, y=35)
    elif len(CompressFolderWaitListListbox.curselection()) == 0:
        ClearLabel = Label(DecompressEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=35)
        NoFileSelectedLabel = Label(DecompressEntryFrame, text='**SELECT A FILE FOR DELETION IN WAIT LIST**', font='OCRAStd 8', bg='lightblue', fg='red')
        NoFileSelectedLabel.place(x=10, y=35)


# Function responsible for removing elements from wait list listbox in Compress Folder.
def CompressFolderRemoveFromWaitList(x):
    CompressFolderHintMessage.destroy()
    if len(CompressFolderWaitListListbox.curselection()) != 0:
        NameList = EditCompressFolderDeleteNameList()
        for item in NameList:
            ClickedList.remove(item)
            CompressFolderWaitListListbox.delete(CompressFolderWaitListListbox.curselection()[0])
            ClearLabel = Label(CompressFolderEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
            ClearLabel.place(x=0, y=35)
            DeleteSuccessfullyLabel = Label(CompressFolderEntryFrame, text='**SUCCESSFULLY DELETED FROM WAIT LIST**', font='OCRAStd 8', bg='lightblue', fg='green')
            DeleteSuccessfullyLabel.place(x=27, y=35)
    elif len(CompressFolderWaitListListbox.curselection()) == 0:
        ClearLabel = Label(CompressFolderEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=35)
        NoFileSelectedLabel = Label(CompressFolderEntryFrame, text='**SELECT A FILE FOR DELETION IN WAIT LIST**', font='OCRAStd 8', bg='lightblue', fg='red')
        NoFileSelectedLabel.place(x=10, y=35)


# Function responsible for removing elements from wait list listbox in Compress File.
def CompressFileRemoveFromWaitList(x):
    CompressFileHintMessage.destroy()
    if len(CompressFileWaitListListbox.curselection()) != 0:
        NameList = EditCompressFileDeleteNameList()
        for item in NameList:
            ClickedList.remove(item)
            CompressFileWaitListListbox.delete(CompressFileWaitListListbox.curselection()[0])
        ClearLabel = Label(CompressFileEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=35)
        DeleteSuccessfullyLabel = Label(CompressFileEntryFrame, text='**SUCCESSFULLY DELETED FROM WAIT LIST**', font='OCRAStd 8', bg='lightblue', fg='green')
        DeleteSuccessfullyLabel.place(x=27, y=35)
    elif len(CompressFileWaitListListbox.curselection()) == 0:
        ClearLabel = Label(CompressFileEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=35)
        NoFileSelectedLabel = Label(CompressFileEntryFrame, text='**SELECT A FILE FOR DELETION IN WAIT LIST**', font='OCRAStd 8', bg='lightblue', fg='red')
        NoFileSelectedLabel.place(x=10, y=35)


# This function destroys the individual and together objects and bind the Return key to a function.
def CompressFileDestroyIndividualTogetherObject():
    CompressFileIndividualButton.destroy()
    CompressFileTogetherButton.destroy()
    IndividualOrTogetherLabel.destroy()
    FirstConfirmLabel.place(x=437, y=265)
    MainWindow.bind('<Return>', FileCompressSetUp)


# This function destroys the individual and together objects and bind the Return key to a function.
def CompressFolderDestroyIndividualTogetherObject():
    CompressFolderIndividualButton.destroy()
    CompressFolderTogetherButton.destroy()
    IndividualOrTogetherLabel.destroy()
    FirstConfirmLabel.place(x=437, y=265)
    MainWindow.bind('<Return>', FolderCompressSetUp)


# This function is responsible for searching ordinary files in disk drives.
def CompressFileSearch():
    SearchFileName = FileName.get()
    if len(SearchFileName) == 0:
        ClearLabel = Label(CompressFileEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=30)
        EntryWarning = Label(CompressFileEntryFrame, text='**TYPE SOMETHING BEFORE YOU PRESS SEARCH**', font='OCRAStd 8', bg='lightblue', fg='red')
        EntryWarning.place(x=10, y=35)
    else:
        FileSearchDirectoryList = []
        DriveList = ['D:/', 'E:/']
        for Drive in DriveList:
            for Root, Directory, Files in os.walk(Drive):
                if SearchFileName in Files:
                    Result = Root + '/' + SearchFileName
                    FileSearchDirectoryList.append(Result)
        if len(FileSearchDirectoryList) == 0:
            ClearLabel = Label(CompressFileEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
            ClearLabel.place(x=0, y=30)
            NoFileFoundWarning = Label(CompressFileEntryFrame, text='**NO FILE FOUND, ENTER SOMETHING CORRECT**', font='OCRAStd 8', bg='lightblue', fg='red')
            NoFileFoundWarning.place(x=10, y=35)
        else:
            ClearLabel = Label(CompressFileEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
            ClearLabel.place(x=0, y=30)
            SetCompressFileListboxFrames(FileSearchDirectoryList)


# This function is responsible for searching folders in disk drives.
def CompressFolderSearch():
    SearchFolderName = FolderName.get()
    if len(SearchFolderName) == 0:
        ClearLabel = Label(CompressFolderEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=30)
        EntryWarning = Label(CompressFolderEntryFrame, text='**TYPE SOMETHING BEFORE YOU PRESS SEARCH**', font='OCRAStd 8', bg='lightblue', fg='red')
        EntryWarning.place(x=10, y=35)
    else:
        FolderSearchDirectoryList = []
        DriveList = ['D:/', 'E:/']
        for Drive in DriveList:
            for Root, Directory, Files in os.walk(Drive):
                if SearchFolderName in Directory:
                    Result = Root + '/' + SearchFolderName
                    FolderSearchDirectoryList.append(Result)
        if len(FolderSearchDirectoryList) == 0:
            ClearLabel = Label(CompressFolderEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
            ClearLabel.place(x=0, y=30)
            NoFileFoundWarning = Label(CompressFolderEntryFrame, text='**NO FOLDER FOUND, ENTER SOMETHING CORRECT**', font='OCRAStd 8', bg='lightblue', fg='red')
            NoFileFoundWarning.place(x=5, y=35)
        else:
            ClearLabel = Label(CompressFolderEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
            ClearLabel.place(x=0, y=30)
            SetCompressFolderListboxFrames(FolderSearchDirectoryList)


# This function is responsible for searching ZIP files in disk drives.
def DecompressFileSearch():
    SearchZipName = ZipFileName.get()
    if len(SearchZipName) == 0:
        ClearLabel = Label(DecompressEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=30)
        EntryWarning = Label(DecompressEntryFrame, text='**TYPE SOMETHING BEFORE YOU PRESS SEARCH**', font='OCRAStd 8', bg='lightblue', fg='red')
        EntryWarning.place(x=10, y=35)
    else:
        ZipFileSearchDirectoryList = []
        DriveList = ['D:/', 'E:/']
        for Drive in DriveList:
            for Root, Directory, Files in os.walk(Drive):
                if SearchZipName + '.zip' in Files:
                    Result = Root + '/' + SearchZipName + '.zip'
                    ZipFileSearchDirectoryList.append(Result)
        if len(ZipFileSearchDirectoryList) == 0:
            ClearLabel = Label(DecompressEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
            ClearLabel.place(x=0, y=30)
            NoFileFoundWarning = Label(DecompressEntryFrame, text='**NO FILE FOUND, ENTER SOMETHING CORRECT**', font='OCRAStd 8', bg='lightblue', fg='red')
            NoFileFoundWarning.place(x=10, y=35)
        else:
            ClearLabel = Label(DecompressEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
            ClearLabel.place(x=0, y=30)
            SetDecompressListboxFrames(ZipFileSearchDirectoryList)


# Decompresses zipfile or zipfiles selected by user.
def Decompress(x):
    if len(DecompressWaitListListbox.get(0, END)) != 0:
        Hit.append(1)
    if len(DecompressWaitListListbox.get(0, END)) == 0:
        ClearLabel = Label(DecompressEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=35)
        NoFileInWaitListLabel = Label(DecompressEntryFrame, text='**ADD SOME FILES TO WAIT LIST PLEASE**', font='OCRAStd 8', bg='lightblue', fg='red')
        NoFileInWaitListLabel.place(x=24, y=35)
    else:
        if len(Hit) == 1:
            SecondConfirmLabel.place(x=437, y=265)
        elif len(Hit) == 2:
            Position = 0
            global InfoList
            InfoList = []
            for ResultDirectory in DecompressWaitListListbox.get(0, END):
                DecompressFileNameListbox.insert(END, ResultDirectory)
            for item in ClickedList:
                CurrentFileInfo = []
                shutil.copy(DecompressWaitListListbox.get(Position), SourceDir + '/' + ClickedList[Position])
                StartTime = time.time()
                ZipFile = zipfile.ZipFile(SourceDir + '/' + ClickedList[Position], 'r')
                Name = EditCompressedFileDirectoryName(ClickedList[Position])
                ZipFile.extractall(DecompressedFileFolderDir + '/' + Name)
                DecompressionTime = time.time() - StartTime
                ZipFile.close()
                CurrentFileInfo.append(EditCompressionTime(DecompressionTime))
                FileDirectory = EditCompressFileDirectory(Name)
                dot = False
                FileDirectory = list(FileDirectory)
                for x in range(len(FileDirectory)-1, 0, -1):
                    if FileDirectory[x] == '.':
                        dot = True
                    FileDirectory[x] = ''
                    if dot:
                        break
                FileDirectory = ''.join(FileDirectory)
                CurrentFileInfo.append(FileDirectory)
                os.remove(SourceDir + '/' + ClickedList[Position])
                Position += 1
                InfoList.append(CurrentFileInfo)
            SetDecompressInformationFrames()


# Prepare for folder compression, determine which compression method to be used by checking the user want to compress
# individually or together.
def FolderCompressSetUp(x):
    if len(CompressFolderWaitListListbox.get(0, END)) != 0:
        Hit.append(1)
    if len(CompressFolderWaitListListbox.get(0, END)) == 0:
        ClearLabel = Label(CompressFolderEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=35)
        NoFileInWaitListLabel = Label(CompressFolderEntryFrame, text='**ADD SOME FILES TO WAITLIST PLEASE**', font='OCRAStd 8', bg='lightblue', fg='red')
        NoFileInWaitListLabel.place(x=24, y=35)
    else:
        if len(Hit) == 1:
            SecondConfirmLabel.place(x=437, y=265)
        elif len(Hit) == 2:
            Position = 0
            global InfoList
            InfoList = []
            if IndividualOrTogether.get() == 'INDIVIDUAL':
                for ResultDirectory in CompressFolderWaitListListbox.get(0, END):
                    CompressFolderFileNameListbox.insert(END, ResultDirectory)
                for item in ClickedList:
                    shutil.copytree(CompressFolderWaitListListbox.get(Position), SourceDir+'/'+ClickedList[Position])
                    Position += 1
                for Index in range(len(ClickedList)):
                    CurrentFolderInfo = []
                    CompressTime = FolderIndividualCompress(SourceDir, Index)
                    try:
                        CurrentFolderInfo.append(CompressTime)
                        for item in CompressFolderWaitListListbox.get(0, END):
                            if ClickedList[Index] in item:
                                CurrentFileDir = item
                        OriginalFolderSize = 0
                        for item in os.listdir(CurrentFileDir):
                            OriginalFolderSize += os.stat(CurrentFileDir+'/'+item).st_size / 1024
                        CurrentFolderInfo.append(OriginalFolderSize)
                        CompressedFolderSize = os.stat(CompressedFileFolderDir + '/' + ClickedList[Index] + '.zip').st_size / 1024
                        CurrentFolderInfo.append(CompressedFolderSize)
                        CompressRatio = CalculateCompressRatio(OriginalFolderSize, CompressedFolderSize)
                        CurrentFolderInfo.append(CompressRatio)
                        CurrentFolderInfo.append(EditCompressFileDirectory(ClickedList[Index]))
                        InfoList.append(CurrentFolderInfo)
                    except FileNotFoundError:
                        CompressFolderShowInFolderButton.place(x=105, y=160)
                SetCompressFolderIndividualFrames()
            else:
                global getListbox
                getListbox = CompressFolderWaitListListbox.get(0, END)
                SetCompressFolderTogetherFrames()


# Prepare for file compression, determine which compression method to be used by checking the user want to compress
# individually or together.
def FileCompressSetUp(x):
    if len(CompressFileWaitListListbox.get(0, END)) != 0:
        Hit.append(1)
    if len(CompressFileWaitListListbox.get(0, END)) == 0:
        ClearLabel = Label(CompressFileEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=35)
        NoFileInWaitListLabel = Label(CompressFileEntryFrame, text='**ADD SOME FILES TO WAIT LIST PLEASE**', font='OCRAStd 8', bg='lightblue', fg='red')
        NoFileInWaitListLabel.place(x=24, y=35)
    else:
        if len(Hit) == 1:
            SecondConfirmLabel.place(x=437, y=265)
        elif len(Hit) == 2:
            EditCompressFileFileName()
            Position = 0
            global InfoList
            InfoList = []
            if IndividualOrTogether.get() == 'INDIVIDUAL':
                for ResultDirectory in CompressFileWaitListListbox.get(0, END):
                    shutil.copy(ResultDirectory, SourceDir)
                    CompressFileFileNameListbox.insert(END, ResultDirectory)
                for EditedFileName in ClickedList:
                    CurrentFileInfo = []
                    CompressionTime = FileIndividualCompress(EditedFileName, Position)
                    CurrentFileInfo.append(CompressionTime)
                    for item in CompressFileWaitListListbox.get(0, END):
                        if EditedFileName in item:
                            CurrentFileDir = item
                    OriginalFileSize = os.stat(CurrentFileDir).st_size / 1024
                    CurrentFileInfo.append(OriginalFileSize)
                    CompressedFileSize = os.stat(CompressedFileFolderDir + '/' + EditedFileName + '.zip').st_size / 1024
                    CurrentFileInfo.append(CompressedFileSize)
                    CompressRatio = CalculateCompressRatio(OriginalFileSize, CompressedFileSize)
                    CurrentFileInfo.append(CompressRatio)
                    CurrentFileInfo.append(EditCompressFileDirectory(EditedFileName))
                    InfoList.append(CurrentFileInfo)
                    Position += 1
                SetCompressFileIndividualFrames()
            else:
                global getListbox
                getListbox = CompressFileWaitListListbox.get(0,END)
                SetCompressFileTogetherFrames()


# This transfer function is called at File and Together selection, when return is hit twice, this function asks the user to name their file.
def CompressFileTogetherTransferFunction():
    Position = 0
    TotalTime = 0
    TotalOriginalSize = 0
    FileNameRepeat = False
    try:
        for ResultDirectory in getListbox:
            shutil.copy(ResultDirectory, SourceDir)
    except FileExistsError:
        None
    for name in os.listdir(CompressedFileFolderDir):
        name = EditCompressedFileDirectoryName(name)
        if ZipName.get() == name:
            FileNameRepeat = True
    if len(ZipName.get()) == 0:
        ClearLabel = Label(CompressFileZipNameEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=45)
        EnterZipNameMessage = Label(CompressFileZipNameEntryFrame, text='**PLEASE NAME YOUR ZIP FILE**', font='OCRAStd 8', bg='lightblue', fg='red')
        EnterZipNameMessage.place(x=60, y=45)
    elif FileNameRepeat:
        ClearLabel = Label(CompressFileZipNameEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=45)
        RepeatZipName = Label(CompressFileZipNameEntryFrame, text='**NAME ALREADY EXISTS, ENTER ANOTHER NAME**', font='OCRAStd 8', bg='lightblue', fg='red')
        RepeatZipName.place(x=5, y=45)
    else:
        ClearLabel = Label(CompressFileZipNameEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=45)
        CompressionCompleteLabel = Label(CompressFileZipNameEntryFrame, text='**COMPRESSION COMPLETED**', font='OCRAStd 8', bg='lightblue', fg='green')
        CompressionCompleteLabel.place(x=75, y=45)
        CompressFileZipNameEntry.configure(state=DISABLED)
        CompressFileZipNameEntryButton.configure(state=DISABLED)
        for EditedFileName in ClickedList:
            ZipFileName = ZipName.get()
            CompressionTime = FileTogetherCompress(ZipFileName, Position)
            TotalTime += float(CompressionTime)
            for item in getListbox:
                if EditedFileName in item:
                    CurrentFileDir = item
            OriginalFileSize = os.stat(CurrentFileDir).st_size / 1024
            TotalOriginalSize += OriginalFileSize
            Position += 1
        CompressedFileSize = os.stat(CompressedFileFolderDir + '/' + ZipName.get() + '.zip').st_size / 1024
        CompressRatio = CalculateCompressRatio(TotalOriginalSize, CompressedFileSize)
        SetCompressFileTogetherInformationFrame(CompressRatio, CompressedFileSize, TotalOriginalSize, TotalTime)


# This transfer function is called at Folder and Together selection, when return is hit twice, this function asks the user to name their file.
def CompressFolderTogetherTransferFunction():
    FileNameRepeat = False
    Index = 0
    try:
        for item in ClickedList:
            shutil.copytree(getListbox[Index], SourceDir + '/' + item)
            Index += 1
    except FileExistsError:
        None
    for name in os.listdir(CompressedFileFolderDir):
        name = EditCompressedFileDirectoryName(name)
        if ZipName.get() == name:
            FileNameRepeat = True
    if len(ZipName.get()) == 0:
        ClearLabel = Label(CompressFolderZipNameEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=45)
        EnterZipNameMessage = Label(CompressFolderZipNameEntryFrame, text='**PLEASE NAME YOUR ZIP FILE**', font='OCRAStd 8', bg='lightblue', fg='red')
        EnterZipNameMessage.place(x=60, y=45)
    elif FileNameRepeat:
        ClearLabel = Label(CompressFolderZipNameEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=45)
        RepeatZipName = Label(CompressFolderZipNameEntryFrame, text='**NAME ALREADY EXISTS, ENTER ANOTHER NAME**', font='OCRAStd 8', bg='lightblue', fg='red')
        RepeatZipName.place(x=5,y=45)
    else:
        ClearLabel = Label(CompressFolderZipNameEntryFrame, text='                                            ', font='OCRAStd 8', bg='lightblue')
        ClearLabel.place(x=0, y=45)
        CompressionCompleteLabel = Label(CompressFolderZipNameEntryFrame, text='**COMPRESSION COMPLETED**', font='OCRAStd 8', bg='lightblue', fg='green')
        CompressionCompleteLabel.place(x=75, y=45)
        CompressFolderZipNameEntry.configure(state=DISABLED)
        CompressFolderZipNameEntryButton.configure(state=DISABLED)
        CompressionTimeAndTotalOriginalFileSize = FolderTogetherCompress()
        CompressionTime = CompressionTimeAndTotalOriginalFileSize[0]
        TotalOriginalFileSize = CompressionTimeAndTotalOriginalFileSize[1]
        CompressedFileSize = os.stat(CompressedFileFolderDir + '/' + ZipName.get() + '.zip').st_size / 1024
        CompressRatio = CalculateCompressRatio(TotalOriginalFileSize, CompressedFileSize)
        SetCompressFolderTogetherInformationFrame(CompressRatio, CompressedFileSize, TotalOriginalFileSize, CompressionTime)


# This function is responsible for compression of File and Individual selection, returns the compression time and total original file size
def FileIndividualCompress(EditedFileName, Position):
    CurrentFileName = FileNameList[Position]
    ZipFile = zipfile.ZipFile(CompressedFileFolderDir + '/' + EditedFileName + '.zip', 'w')
    StartTime = time.time()
    ZipFile.write(CurrentFileName, compress_type=zipfile.ZIP_DEFLATED)
    CompressionTime = time.time() - StartTime
    ZipFile.close()
    os.remove(CurrentFileName)
    return EditCompressionTime(CompressionTime)


# This function is responsible for compression of Folder and Together selection, returns the compression time and total original file size
def FileTogetherCompress(ZipFileName, Position):
    CurrentFileName = FileNameList[Position]
    ZipFile = zipfile.ZipFile(CompressedFileFolderDir + '/' + ZipFileName + '.zip', 'a')
    StartTime = time.time()
    ZipFile.write(CurrentFileName, compress_type=zipfile.ZIP_DEFLATED)
    CompressionTime = time.time() - StartTime
    ZipFile.close()
    os.remove(CurrentFileName)
    return EditCompressionTime(CompressionTime)


# This function is responsible for compression of File and Individual selection, returns the compression time and total original file size
def FolderIndividualCompress(SourceDir, Index):
    ZipFile = zipfile.ZipFile(CompressedFileFolderDir + '/' + ClickedList[Index] + '.zip', 'w')
    StartTime = time.time()
    for item in os.listdir(SourceDir + '/' + ClickedList[Index]):
        if os.path.isfile(SourceDir+'/'+ClickedList[Index]+'/'+item):
            shutil.move(SourceDir + '/' + ClickedList[Index] + '/' + item, SourceDir)
            ZipFile.write(item, compress_type=zipfile.ZIP_DEFLATED)
            os.remove(SourceDir + '/' + item)
    shutil.rmtree(SourceDir + '/' + ClickedList[Index])
    ZipFile.close()
    CompressionTime = time.time() - StartTime
    return EditCompressionTime(CompressionTime)


# This function is responsible for compression of File and Together selection, returns the compression time and total original file size
def FolderTogetherCompress():
    ZipFileName = ZipName.get()
    ZipFile = zipfile.ZipFile(CompressedFileFolderDir + '/' + ZipFileName + '.zip', 'a')
    TotalOriginalFileSize = 0
    StartTime = time.time()
    for CurrentFolder in ClickedList:
        for item in os.listdir(SourceDir + '/' + CurrentFolder):
            if os.path.isfile(SourceDir + '/' + CurrentFolder + '/' + item):
                shutil.copy(SourceDir + '/' + CurrentFolder + '/' + item, SourceDir)
                TotalOriginalFileSize += os.stat(SourceDir + '/' + item).st_size / 1024
                ZipFile.write(item, CurrentFolder + '/' + item, compress_type=zipfile.ZIP_DEFLATED)
                os.remove(SourceDir + '/' + item)
        shutil.rmtree(SourceDir + '/' + CurrentFolder)
    CompressionTime = time.time() - StartTime
    return EditCompressionTime(CompressionTime), TotalOriginalFileSize


def EditDecompressDeleteNameList():
    ZipFileToBeDeleted = DecompressWaitListListbox.curselection()
    NameList = []
    for item in ZipFileToBeDeleted:
        ListedFile = DecompressWaitListListbox.get(item)
        Dash = False
        Index = len(ListedFile)
        Name = []
        while not Dash:
            if ListedFile[Index-1] != '/' and ListedFile[Index-1] != '\\':
                Name.append(ListedFile[Index-1])
            else:
                Dash = True
            Index -= 1
        Name.reverse()
        Name = ''.join(Name)
        NameList.append(Name)
    return NameList


def EditCompressFileDeleteNameList():
    FileToBeDeleted = CompressFileWaitListListbox.curselection()
    NameList = []
    for item in FileToBeDeleted:
        ListedFile = CompressFileWaitListListbox.get(item)
        Dash = False
        Index = len(ListedFile)
        Name = []
        while not Dash:
            if ListedFile[Index-1] != '/' and ListedFile[Index-1] != '\\':
                Name.append(ListedFile[Index-1])
            else:
                Dash = True
            Index -= 1
        Name.reverse()
        Name = ''.join(Name)
        NameList.append(Name)
    return NameList


def EditCompressFolderDeleteNameList():
    FolderToBeDeleted = CompressFolderWaitListListbox.curselection()
    NameList = []
    for item in FolderToBeDeleted:
        ListedFile = CompressFolderWaitListListbox.get(item)
        Dash = False
        Index = len(ListedFile)
        Name = []
        while not Dash:
            if ListedFile[Index-1] != '/' and ListedFile[Index-1] != '\\':
                Name.append(ListedFile[Index-1])
            else:
                Dash = True
            Index -= 1
        Name.reverse()
        Name = ''.join(Name)
        NameList.append(Name)
    return NameList


# Takes in a zipfile directory and edits the directory and return the name of the zipfile in that directory for the purpose
# of adding the name to wait list.
def EditDecompressAddToWaitListName():
    ZipFileToBeAdded = DecompressSearchResultListbox.get(DecompressSearchResultListbox.curselection())
    Dash = False
    Index = len(ZipFileToBeAdded)
    Name = []
    while not Dash:
        if ZipFileToBeAdded[Index-1] != '/' and ZipFileToBeAdded[Index-1] != '\\':
            Name.append(ZipFileToBeAdded[Index-1])
        else:
            Dash = True
        Index -= 1
    Name.reverse()
    Name = ''.join(Name)
    return Name


# Takes in a file directory and edits the directory and return the name of the file in that directory for the purpose
# of adding the name to wait list.
def EditCompressFileAddToWaitListName():
    FileToBeAdded = CompressFileSearchResultListbox.get(CompressFileSearchResultListbox.curselection())
    Dash = False
    Index = len(FileToBeAdded)
    Name = []
    while not Dash:
        if FileToBeAdded[Index-1] != '/' and FileToBeAdded[Index-1] != '\\':
            Name.append(FileToBeAdded[Index-1])
        else:
            Dash = True
        Index -= 1
    Name.reverse()
    Name = ''.join(Name)
    return Name


# Takes in a folder directory and edits the directory and return the name of the folder in that directory for the purpose
# of adding the name to wait list.
def EditCompressFolderAddToWaitListName():
    FolderToBeAdded = CompressFolderSearchResultListbox.get(CompressFolderSearchResultListbox.curselection())
    Dash = False
    Index = len(FolderToBeAdded)
    Name = []
    while not Dash:
        if FolderToBeAdded[Index-1] != '/' and FolderToBeAdded[Index-1] != '\\':
            Name.append(FolderToBeAdded[Index-1])
        else:
            Dash = True
        Index -= 1
    Name.reverse()
    Name = ''.join(Name)
    return Name


# This function edits the file name so that maximum 9 characters can be be taken, if the file name is larger than 9
# characters then the rest will be represented as '...'
def EditEntryFileName():
    if len(FileName.get()) == 0:
        if len(ZipFileName.get()) == 0:
            EntryFileName = list(FolderName.get())
        else:
            EntryFileName = list(ZipFileName.get())
    else:
        EntryFileName = list(FileName.get())
    if len(EntryFileName) > 9:
        for x in range(len(EntryFileName) - 1, 8, -1):
            EntryFileName[x] = ''
        EntryFileName = ''.join(EntryFileName)
        EntryFileName += '...'
    else:
        EntryFileName = ''.join(EntryFileName)
    return EntryFileName


# This function edits a file directory and gets rid of the file type at the end of the directory.
# Such as turning C:/Users/..../Music.jpg into C:/Users/.../Music
def EditCompressedFileDirectoryName(name):
    name = list(name)
    dot = False
    for x in range(len(name)):
        if name[x] == '.':
            dot = True
        if dot:
            name[x] = ''
    name = ''.join(name)
    return name


# This function turns the name of a file in form like <Further Maths.pdf> into form <Further Maths>.
def EditCompressFileFileName():
    for Index in range(len(ClickedList)):
        CurrentItem = ClickedList[Index]
        FileNameList.append(CurrentItem)
        CurrentItem = list(CurrentItem)
        dot = False
        for x in range(len(CurrentItem)):
            if CurrentItem[x] == '.':
                dot = True
            if dot:
                CurrentItem[x] = ''
        CurrentItem = ''.join(CurrentItem)
        ClickedList[Index] = CurrentItem
    return ClickedList


# Function that edits the compression time and make it into a two decimal place number.
def EditCompressionTime(CompressionTime):
    CompressionTime = str(CompressionTime)
    CompressionTime = list(CompressionTime)
    EditedCompressionTime = ''
    for x in range(len(CompressionTime)):
        if CompressionTime[x] != '.':
            EditedCompressionTime += CompressionTime[x]
        else:
            EditedCompressionTime += CompressionTime[x] + CompressionTime[x + 1] + CompressionTime[x + 2]
            break
    return EditedCompressionTime


# Function that takes in the entire directory of the compressed zip file so the directory is in a form that fits the frame.
def EditCompressFileDirectory(EditedFileName):
    CompressedFileDirectory = CompressedFileFolderDir + '/' + EditedFileName + '.zip'
    Repeats = len(CompressedFileDirectory) // 40
    Position = 0
    List = []
    while Repeats != -1 and Position < len(CompressedFileDirectory):
        if Position % 39 == 0 and Position != 0:
            List.append('\n')
            Repeats -= 1
        List.append(CompressedFileDirectory[Position])
        Position += 1
    CompressedFileDirectory = ''.join(List)
    return CompressedFileDirectory


# Function that takes in original file size and compressed file size and calculate and return the compression ratio as a percentage.
def CalculateCompressRatio(OriginalFileSize, CompressedFileSize):
    CompressRatio = (1 - (CompressedFileSize / OriginalFileSize)) * 100
    CompressRatio = str(CompressRatio)
    CompressRatio = list(CompressRatio)
    EditedCompressRatio = ''
    for x in range(len(CompressRatio)):
        if CompressRatio[x] != '.':
            EditedCompressRatio += CompressRatio[x]
        else:
            EditedCompressRatio += CompressRatio[x] + CompressRatio[x + 1]
            break
    EditedCompressRatio = str(EditedCompressRatio) + ' %'
    return EditedCompressRatio


# Configuration of the main window.
MainWindow = Tk()
MainWindow.title('Compress & Decompress Application')
MainWindow.geometry('400x315+450+200')
MainWindow.configure(bg='lightblue')
MainWindow.resizable(0, 0)


# Initialising all widgets needed：
# Creating Frame:
CompOrDecompFrame = LabelFrame(MainWindow, text='Do you want to compress\nor decompress?', font='OCRAStd 9', width=367, height=215, bg='lightblue')
FolderOrFileFrame = LabelFrame(MainWindow, text='Do you want to process\nfolders or files?', font='OCRAStd 9', width=367, height=215, bg='lightblue')
CompressFileEntryFrame = LabelFrame(MainWindow, text='Enter file name in form\n [name].[filetype] (eg:examplefile.pdf)', font='OCRAStd 9', width=367, height=215, bg='lightblue')
CompressFileWaitListListboxFrame = LabelFrame(MainWindow, text='Wait List', font='OCRAStd 9', height=215, width=275, padx=5, pady=3, bg='lightblue')
CompressFileSearchResultListboxFrame = LabelFrame(MainWindow, text='Search result', font='OCRAStd 9', height=100, width=275, padx=5, pady=3, bg='lightblue')
CompressFileIndividualListboxFrame = LabelFrame(MainWindow, text='DOUBLE CLICK a file to\nview its compression info', font='OCRAStd 9', width=367, height=215, bg='lightblue')
CompressFileInformationFrame = LabelFrame(MainWindow, text='Compression Information', font='OCRAStd 9', height=215, width=367, padx=5, pady=3, bg='lightblue')
CompressFileZipNameEntryFrame = LabelFrame(MainWindow, text='Name your ZIP file', font='OCRAStd 9', width=367, height=215, bg='lightblue')
CompressFolderEntryFrame = LabelFrame(MainWindow, text='Enter name of the folder\nyou want to compress', font='OCRAStd 9', width=367, height=215, bg='lightblue')
CompressFolderWaitListListboxFrame = LabelFrame(MainWindow, text='Wait List', font='OCRAStd 9', height=215, width=275, padx=5, pady=3, bg='lightblue')
CompressFolderSearchResultListboxFrame = LabelFrame(MainWindow, text='Search result', font='OCRAStd 9', height=100, width=275, padx=5, pady=3, bg='lightblue')
CompressFolderIndividualListboxFrame = LabelFrame(MainWindow, text='DOUBLE CLICK a file to\nview its compression info', font='OCRAStd 9', width=367, height=215, bg='lightblue')
CompressFolderInformationFrame = LabelFrame(MainWindow, text='Compression Information', font='OCRAStd 9', height=215, width=367, padx=5, pady=3, bg='lightblue')
CompressFolderZipNameEntryFrame = LabelFrame(MainWindow, text='Name your ZIP file', font='OCRAStd 9', width=367, height=215, bg='lightblue')
DecompressEntryFrame = LabelFrame(MainWindow, text='Enter name of the ZIP folder\nyou want to decompress',  font='OCRAStd 9', width=367, height=215, bg='lightblue')
DecompressWaitListListboxFrame = LabelFrame(MainWindow, text='Wait List', font='OCRAStd 9', height=215, width=275, padx=5, pady=3, bg='lightblue')
DecompressSearchResultListboxFrame = LabelFrame(MainWindow, text='Search result', font='OCRAStd 9', height=100, width=275, padx=5, pady=3, bg='lightblue')
DecompressIndividualListboxFrame = LabelFrame(MainWindow, text='DOUBLE CLICK a ZIP file to\nview its decompression info', font='OCRAStd 9', width=367, height=215, bg='lightblue')
DecompressInformationFrame = LabelFrame(MainWindow, text='Decompression Information', font='OCRAStd 9', height=215, width=367, padx=5, pady=3, bg='lightblue')


# Creating String variable:
FolderName = StringVar()
FileName = StringVar()
CompOrDecomp = StringVar()
FolderOrFile = StringVar()
IndividualOrTogether = StringVar()
ZipName = StringVar()
ZipFileName = StringVar()
ClickedList = []
FileNameList = []
Hit = []
getListbox = []
InfoList = []


# Creating Labels:
WelcomeMessage = Label(MainWindow, text='Welcome to Compression &\n Decompression Application', font='HoboStd 18', bg='lightblue')
WelcomeMessage.place(x=45, y=8)
IndividualOrTogetherLabel = Label(MainWindow, text='DO YOU WANT THE FILES    -->\nIN WAITLIST TO BE COMPRESSED\nINDIVIDUALLY OR ALL TOGETHER?', font='OCRAStd 8', bg='lightblue')
FirstConfirmLabel = Label(MainWindow, text='HIT RETURN **TWICE** TO CONFIRM\nCOMPRESSION OF FILES IN WAITLIST', font='OCRAStd 8', bg='lightblue', )
SecondConfirmLabel = Label(MainWindow, text='HIT RETURN ONCE MORE TO CONFIRM\nCOMPRESSION OF FILES IN WAITLIST', font='OCRAStd 8', bg='lightblue', fg='green')
CompressFileHintMessage = Label(CompressFileEntryFrame, text='HINT: TO REMOVE FILES IN WAITLIST,\n        SELECT FILES AND PRESS DELETE.', font='OCRAStd 7', bg='lightblue')
CompressFolderHintMessage = Label(CompressFolderEntryFrame, text='HINT: TO REMOVE FOLDERS IN WAITLIST,\n        SELECT FILES AND PRESS DELETE.', font='OCRAStd 7', bg='lightblue')
DecompressHintMessage = Label(CompressFolderEntryFrame, text='HINT: TO REMOVE FILES IN WAITLIST,\n        SELECT FILES AND PRESS DELETE.', font='OCRAStd 7', bg='lightblue')


# Creating Buttons:
CompressButton = Button(CompOrDecompFrame, text='COMPRESS', activebackground='lightgrey', command=SetComp, bd=5, padx=12, pady=30, font='OCRAStd 12')
CompressButton.place(x=25, y=40)
DecompressButton = Button(CompOrDecompFrame, text='DECOMPRESS', activebackground='lightgrey', command=SetDecomp, bd=5, padx=0, pady=30, font='OCRAStd 12')
DecompressButton.place(x=195, y=40)
FolderButton = Button(FolderOrFileFrame, text='Folder', activebackground='lightgrey', command=SetFolder, bd=5, padx=24, pady=30, font='OCRAStd 12')
FolderButton.place(x=25, y=40)
FileButton = Button(FolderOrFileFrame, text='File', activebackground='lightgrey', command=SetFile, bd=5, padx=36, pady=30, font='OCRAStd 12')
FileButton.place(x=195, y=40)
CompressFileSearchButton = Button(CompressFileEntryFrame, text='SEARCH', activebackground='lightgrey', command=CompressFileSearch, padx=10, font='OCRAStd 9')
CompressFileSearchButton.place(x=138, y=110)
CompressFileIndividualButton = Button(MainWindow, text='INDIVIDUAL', activebackground='lightgrey', command=SetCompressFileIndividual, font='OCRAStd 9')
CompressFileTogetherButton = Button(MainWindow, text='TOGETHER', activebackground='lightgrey', command=SetCompressFileTogether, padx=10, font='OCRAStd 9')
CompressFileShowInFolderButton = Button(CompressFileInformationFrame, text='SHOW IN FOLDER', activebackground='lightgrey', command=lambda: os.startfile(CompressedFileFolderDir), font='OCRAStd 9')
CompressFileZipNameEntryButton = Button(CompressFileZipNameEntryFrame, text='COMPRESS', activebackground='lightgrey', command=CompressFileTogetherTransferFunction, font='OCRAStd 9')
CompressFileZipNameEntryButton.place(x=138, y=123)
CompressFolderSearchButton = Button(CompressFolderEntryFrame, text='SEARCH', activebackground='lightgrey', command=CompressFolderSearch, padx=10, font='OCRAStd 9')
CompressFolderSearchButton.place(x=138, y=110)
CompressFolderIndividualButton = Button(MainWindow, text='INDIVIDUAL', activebackground='lightgrey', command=SetCompressFolderIndividual, font='OCRAStd 9')
CompressFolderTogetherButton = Button(MainWindow, text='TOGETHER', activebackground='lightgrey', command=SetCompressFolderTogether, padx=10, font='OCRAStd 9')
CompressFolderShowInFolderButton = Button(CompressFolderInformationFrame, text='SHOW IN FOLDER', activebackground='lightgrey', command=lambda: os.startfile(CompressedFileFolderDir), font='OCRAStd 9')
CompressFolderZipNameEntryButton = Button(CompressFolderZipNameEntryFrame, text='COMPRESS', command=CompressFolderTogetherTransferFunction, activebackground='lightgrey', font='OCRAStd 9')
CompressFolderZipNameEntryButton.place(x=138, y=123)
DecompressSearchButton = Button(DecompressEntryFrame, text='SEARCH', activebackground='lightgrey', command=DecompressFileSearch, padx=10, font='OCRAStd 9')
DecompressSearchButton.place(x=138, y=110)
DecompressShowInFolderButton = Button(DecompressInformationFrame, text='SHOW IN FOLDER', activebackground='lightgrey', command=lambda: os.startfile(DecompressedFileFolderDir), font='OCRAStd 9')


# Creating Entry:
CompressFileEntry = Entry(CompressFileEntryFrame, width=40, textvariable=FileName)
CompressFileEntry.place(x=39, y=60)
CompressFolderEntry = Entry(CompressFolderEntryFrame, width=40, textvariable=FolderName)
CompressFolderEntry.place(x=39, y=60)
CompressFileZipNameEntry = Entry(CompressFileZipNameEntryFrame, width=40, textvariable=ZipName)
CompressFileZipNameEntry.place(x=39, y=73)
CompressFolderZipNameEntry = Entry(CompressFolderZipNameEntryFrame, width=40, textvariable=ZipName)
CompressFolderZipNameEntry.place(x=39, y=73)
DecompressEntry = Entry(DecompressEntryFrame, width=40, textvariable=ZipFileName)
DecompressEntry.place(x=39, y=60)


# Creating Scrollbars:
CompressFileXScrollbar1 = Scrollbar(CompressFileWaitListListboxFrame, orient=HORIZONTAL)
CompressFileXScrollbar1.pack(side=BOTTOM, fill=X)
CompressFileYScrollbar1 = Scrollbar(CompressFileWaitListListboxFrame)
CompressFileYScrollbar1.pack(side=RIGHT, fill=Y)
CompressFileXScrollbar2 = Scrollbar(CompressFileSearchResultListboxFrame, orient=HORIZONTAL)
CompressFileXScrollbar2.pack(side=BOTTOM, fill=X)
CompressFileYScrollbar2 = Scrollbar(CompressFileSearchResultListboxFrame)
CompressFileYScrollbar2.pack(side=RIGHT, fill=Y)
CompressFileFileNameXScrollbar = Scrollbar(CompressFileIndividualListboxFrame, orient=HORIZONTAL)
CompressFileFileNameXScrollbar.pack(side=BOTTOM, fill=X)
CompressFileFileNameYScrollbar = Scrollbar(CompressFileIndividualListboxFrame)
CompressFileFileNameYScrollbar.pack(side=RIGHT, fill=Y)
CompressFolderXScrollbar1 = Scrollbar(CompressFolderWaitListListboxFrame, orient=HORIZONTAL)
CompressFolderXScrollbar1.pack(side=BOTTOM, fill=X)
CompressFolderYScrollbar1 = Scrollbar(CompressFolderWaitListListboxFrame)
CompressFolderYScrollbar1.pack(side=RIGHT, fill=Y)
CompressFolderXScrollbar2 = Scrollbar(CompressFolderSearchResultListboxFrame, orient=HORIZONTAL)
CompressFolderXScrollbar2.pack(side=BOTTOM, fill=X)
CompressFolderYScrollbar2 = Scrollbar(CompressFolderSearchResultListboxFrame)
CompressFolderYScrollbar2.pack(side=RIGHT, fill=Y)
CompressFolderFileNameXScrollbar = Scrollbar(CompressFolderIndividualListboxFrame, orient=HORIZONTAL)
CompressFolderFileNameXScrollbar.pack(side=BOTTOM, fill=X)
CompressFolderFileNameYScrollbar = Scrollbar(CompressFolderIndividualListboxFrame)
CompressFolderFileNameYScrollbar.pack(side=RIGHT, fill=Y)
DecompressXScrollbar1 = Scrollbar(DecompressWaitListListboxFrame, orient=HORIZONTAL)
DecompressXScrollbar1.pack(side=BOTTOM, fill=X)
DecompressYScrollbar1 = Scrollbar(DecompressWaitListListboxFrame)
DecompressYScrollbar1.pack(side=RIGHT, fill=Y)
DecompressXScrollbar2 = Scrollbar(DecompressSearchResultListboxFrame, orient=HORIZONTAL)
DecompressXScrollbar2.pack(side=BOTTOM, fill=X)
DecompressYScrollbar2 = Scrollbar(DecompressSearchResultListboxFrame)
DecompressYScrollbar2.pack(side=RIGHT, fill=Y)
DecompressFileNameXScrollbar = Scrollbar(DecompressIndividualListboxFrame, orient=HORIZONTAL)
DecompressFileNameXScrollbar.pack(side=BOTTOM, fill=X)
DecompressFileNameYScrollbar = Scrollbar(DecompressIndividualListboxFrame)
DecompressFileNameYScrollbar.pack(side=RIGHT, fill=Y)


# Creating Listbox:
CompressFileWaitListListbox = Listbox(CompressFileWaitListListboxFrame, height=5, width=35, xscrollcommand=CompressFileXScrollbar1.set, yscrollcommand=CompressFileYScrollbar1.set, selectmode=MULTIPLE, font='OCRAStd 10')
CompressFileWaitListListbox.pack(side=LEFT, fill=X)
CompressFileSearchResultListbox = Listbox(CompressFileSearchResultListboxFrame, height=5, width=35, xscrollcommand=CompressFileXScrollbar2.set, yscrollcommand=CompressFileYScrollbar2.set, selectmode=SINGLE, font='OCRAStd 10')
CompressFileSearchResultListbox.pack(side=LEFT, fill=X)
CompressFileFileNameListbox = Listbox(CompressFileIndividualListboxFrame, height=11, width=38, xscrollcommand=CompressFileFileNameXScrollbar.set, yscrollcommand=CompressFileFileNameYScrollbar.set, selectmode=SINGLE, font='OCRAStd 10')
CompressFileFileNameListbox.pack(side=LEFT, fill=X)
CompressFolderWaitListListbox = Listbox(CompressFolderWaitListListboxFrame, height=5, width=35, xscrollcommand=CompressFolderXScrollbar1.set, yscrollcommand=CompressFolderYScrollbar1.set, selectmode=MULTIPLE, font='OCRAStd 10')
CompressFolderWaitListListbox.pack(side=LEFT, fill=X)
CompressFolderSearchResultListbox = Listbox(CompressFolderSearchResultListboxFrame, height=5, width=35, xscrollcommand=CompressFolderXScrollbar2.set, yscrollcommand=CompressFolderYScrollbar2.set, selectmode=SINGLE, font='OCRAStd 10')
CompressFolderSearchResultListbox.pack(side=LEFT, fill=X)
CompressFolderFileNameListbox = Listbox(CompressFolderIndividualListboxFrame, height=11, width=38, xscrollcommand=CompressFolderFileNameXScrollbar.set, yscrollcommand=CompressFolderFileNameYScrollbar.set, selectmode=SINGLE, font='OCRAStd 10')
CompressFolderFileNameListbox.pack(side=LEFT, fill=X)
DecompressWaitListListbox = Listbox(DecompressWaitListListboxFrame, height=5, width=35, xscrollcommand=DecompressXScrollbar1.set, yscrollcommand=DecompressYScrollbar1.set, selectmode=MULTIPLE, font='OCRAStd 10')
DecompressWaitListListbox.pack(side=LEFT, fill=X)
DecompressSearchResultListbox = Listbox(DecompressSearchResultListboxFrame, height=5, width=35, xscrollcommand=DecompressXScrollbar2.set, yscrollcommand=DecompressYScrollbar2.set, selectmode=SINGLE, font='OCRAStd 10')
DecompressSearchResultListbox.pack(side=LEFT, fill=X)
DecompressFileNameListbox = Listbox(DecompressIndividualListboxFrame, height=11, width=38, xscrollcommand=DecompressFileNameXScrollbar.set, yscrollcommand=DecompressFileNameYScrollbar.set, selectmode=SINGLE, font='OCRAStd 10')
DecompressFileNameListbox.pack(side=LEFT, fill=X)


# Attaching scrollbars to listbox
CompressFileXScrollbar1.config(command=CompressFileWaitListListbox.xview)
CompressFileYScrollbar1.config(command=CompressFileWaitListListbox.yview)
CompressFileXScrollbar2.config(command=CompressFileSearchResultListbox.xview)
CompressFileYScrollbar2.config(command=CompressFileSearchResultListbox.yview)
CompressFileFileNameXScrollbar.config(command=CompressFileFileNameListbox.xview)
CompressFileFileNameYScrollbar.config(command=CompressFileFileNameListbox.yview)
CompressFolderXScrollbar1.config(command=CompressFolderWaitListListbox.xview)
CompressFolderYScrollbar1.config(command=CompressFolderWaitListListbox.yview)
CompressFolderXScrollbar2.config(command=CompressFolderSearchResultListbox.xview)
CompressFolderYScrollbar2.config(command=CompressFolderSearchResultListbox.yview)
CompressFolderFileNameXScrollbar.config(command=CompressFolderFileNameListbox.xview)
CompressFolderFileNameYScrollbar.config(command=CompressFolderFileNameListbox.yview)
DecompressXScrollbar1.config(command=DecompressWaitListListbox.xview)
DecompressYScrollbar1.config(command=DecompressWaitListListbox.yview)
DecompressXScrollbar2.config(command=DecompressSearchResultListbox.xview)
DecompressYScrollbar2.config(command=DecompressSearchResultListbox.yview)
DecompressFileNameXScrollbar.config(command=DecompressFileNameListbox.xview)
DecompressFileNameYScrollbar.config(command=DecompressFileNameListbox.yview)


# Calling the first frame
SetCompOrDecompFrame()


# Creating a folder at the same directory as code called ProcessedFiles which stores all compressed and decompressed files
SourceDir = list(sys.argv[0])
Stop = False
for i in range(len(SourceDir) - 1, 0, -1):
    if SourceDir[i] == '/' or SourceDir[i] == '\\':
        SourceDir[i] = ''
        break
    else:
        SourceDir[i] = ''
SourceDir = ''.join(SourceDir)

try:
    os.chdir(SourceDir)
    os.mkdir('Processed Files')
except FileExistsError:
    None


# Creating two folders - Compressed Files and Decompressed Files within the folder ProcessedFiles
CompDecompFilesDirectory = SourceDir + '/Processed Files'
try:
    os.chdir(CompDecompFilesDirectory)
    os.mkdir('Compressed Files')
    os.mkdir('Decompressed Files')
except FileExistsError:
    None


# variables that saves the directory of CompressedFiles, DecompressedFiles and Cache
CompressedFileFolderDir = CompDecompFilesDirectory + '/Compressed Files'
DecompressedFileFolderDir = CompDecompFilesDirectory + '/Decompressed Files'

os.chdir(SourceDir)

MainWindow.mainloop()