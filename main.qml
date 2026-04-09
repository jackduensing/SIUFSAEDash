import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Window 2.15
import QtQuick.Layouts 2.15

Window{

    id: root
    visible: true
    visibility: Window.FullScreen
    title: "GUI"

    SwipeView{

        id: swipeRoot
        anchors.fill: parent
        currentIndex: 0

        page1 {}
        page2 {}

    }

}