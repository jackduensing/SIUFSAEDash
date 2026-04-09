import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 2.15

Window{

    id: root
    visible: true
    visibility: Window.FullScreen
    title: "GUI"

    Timer{
        interval: 1000
        running: true
        repeat: true
        onTriggered: timeText.text = Qt.formatTime(new Date(), "hh:mm:ss")
    }

    Item {

        id: rotateItem
        rotation: 90
        width: Screen.height
        height: Screen.width
        anchors.fill: parent
        

        ColumnLayout{
            anchors.fill: parent
            spacing: 0

            //rpm bar
            RowLayout{
                id: rpmBar
                spacing: 0
                Layout.fillWidth: true
                Layout.preferredHeight: Screen.height * 0.2
                Layout.maximumHeight: Screen.height * 0.2


                Rectangle{
                    id: rpm1
                    color: backend.rpm > 0 ? "green" : "white"
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                }

                Rectangle{
                    id: rpm2
                    color: backend.rpm > 2000 ? "green" : "white"
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                }

                Rectangle{
                    id: rpm3
                    color: backend.rpm > 4000 ? "green" : "white"
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                }

                Rectangle{
                    id: rpm4
                    color: backend.rpm > 6000 ? "green" : "white"
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                }

                Rectangle{
                    id: rpm5
                    color: backend.rpm > 8000 ? "green" : "white"
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                }

                Rectangle{
                    id: rpm6
                    color: backend.rpm > 10000 ? "green" : "white"
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                }

                Rectangle{
                    id: rpm7
                    color: backend.rpm > 12000 ? "green" : "white"
                    Layout.fillWidth: true
                    Layout.fillHeight: true
                }
            }

            //rpm value indicator
            RowLayout{
                id: rpmValueRow
                Layout.fillWidth: true
                Layout.preferredHeight: Screen.height * 0.3
                Layout.maximumHeight: Screen.height * 0.3

                Rectangle{
                    id: rpmValueBox
                    color: "transparent"
                    Layout.fillWidth: true
                    Layout.fillHeight: true

                    Text{
                        id: rpmTextBox
                        anchors.fill: parent
                        color: "#800000"
                        text: backend.rpm
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }
            }

            //spacer
            Item{
                Layout.fillWidth: true
                Layout.preferredHeight: Screen.height * 0.1
                Layout.maximumHeight: Screen.height * 0.1
            }  

            //others bar
            GridLayout{
                id: othersRow
                Layout.fillWidth: true
                Layout.preferredHeight: Screen.height * 0.2
                Layout.maximumHeight: Screen.height * 0.2
                columns: 3

                Rectangle{
                    id: cltValueBox
                    color: "transparent"
                    Layout.fillWidth: true
                    Layout.fillHeight: true

                    Text{
                        id: cltBox
                        anchors.fill: parent
                        color: "#800000"
                        text: backend.clt
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }

                Rectangle{
                    id: gearValueBox
                    color: "transparent"
                    Layout.fillWidth: true
                    Layout.fillHeight: true

                    Text{
                        id: gearBox
                        anchors.fill: parent
                        color: "#800000"
                        text: backend.gear
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }

                Rectangle{
                    id: battValueBox
                    color: "transparent"
                    Layout.fillWidth: true
                    Layout.fillHeight: true

                    Text{
                        id: battBox
                        anchors.fill: parent
                        color: "#800000"
                        text: backend.batt
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }

                Rectangle{
                    id: cltLabelBox
                    color: "transparent"
                    Layout.fillWidth: true
                    Layout.fillHeight: true

                    Text{
                        id: cltTextBox
                        anchors.fill: parent
                        color: "#800000"
                        text: "Clt (C)"
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }

                Rectangle{
                    id: gearLabelBox
                    color: "transparent"
                    Layout.fillWidth: true
                    Layout.fillHeight: true

                    Text{
                        id: gearTextBox
                        anchors.fill: parent
                        color: "#800000"
                        text: "Gear"
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }

                Rectangle{
                    id: battLabelBox
                    color: "transparent"
                    Layout.fillWidth: true
                    Layout.fillHeight: true

                    Text{
                        id: battTextBox
                        anchors.fill: parent
                        color: "#800000"
                        text: "Batt (V)"
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }
            }

            //spacer
            Item{
                Layout.fillWidth: true
                Layout.preferredHeight: Screen.height * 0.125
                Layout.maximumHeight: Screen.height * 0.125
            }

            //time footer
            RowLayout{
                id: timeRow
                Layout.fillWidth: true
                Layout.preferredHeight: Screen.height * 0.05
                Layout.maximumHeight: Screen.height * 0.05

                Rectangle{
                    id: timeBox
                    color: "transparent"
                    Layout.fillWidth: true
                    Layout.fillHeight: true

                    Text{
                        id: timeText
                        anchors.fill: parent
                        color: "black"
                        text: Qt.formatTime(new Date(), "hh:mm:ss")
                        fontSizeMode: Text.Fit
                        font.pixelSize: 1000
                        minimumPixelSize: 10
                        horizontalAlignment: Text.AlignHCenter
                        verticalAlignment: Text.AlignVCenter
                    }
                }
            }

            //spacer
            Item{
                Layout.fillWidth: true
                Layout.preferredHeight: Screen.height * 0.025
                Layout.maximumHeight: Screen.height * 0.025
            }
        }
    }
}
