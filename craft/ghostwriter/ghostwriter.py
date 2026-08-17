import info

from Package.CMakePackageBase import CMakePackageBase


class subinfo(info.infoclass):

    def setTargets(self):
        self.displayName = "ghostwriter"
        self.description = "Text editor for Markdown"
        self.webpage = "https://github.com/KDE/ghostwriter"

        self.svnTargets["master"] = \
            "https://github.com/KDE/ghostwriter.git|master"

        self.defaultTarget = "master"

    def setDependencies(self):
        self.buildDependencies[
            "kde/frameworks/extra-cmake-modules"
        ] = None

        # Qt 6
        self.runtimeDependencies["libs/qt/qtbase"] = None
        self.runtimeDependencies["libs/qt/qtsvg"] = None
        self.runtimeDependencies["libs/qt/qttools"] = None
        self.runtimeDependencies["libs/qt/qtwebchannel"] = None
        self.runtimeDependencies["libs/qt/qtwebengine"] = None

        # KDE Frameworks 6
        self.runtimeDependencies[
            "kde/frameworks/tier1/kcoreaddons"
        ] = None

        self.runtimeDependencies[
            "kde/frameworks/tier1/kwidgetsaddons"
        ] = None

        self.runtimeDependencies[
            "kde/frameworks/tier1/sonnet"
        ] = None

        self.runtimeDependencies[
            "kde/frameworks/tier2/kconfig"
        ] = None

        self.runtimeDependencies[
            "kde/frameworks/tier3/kconfigwidgets"
        ] = None

        self.runtimeDependencies[
            "kde/frameworks/tier3/kxmlgui"
        ] = None

        self.runtimeDependencies[
            "kde/frameworks/tier3/kiconthemes"
        ] = None

        self.runtimeDependencies[
            "kde/frameworks/tier1/breeze-icons"
        ] = None


class Package(CMakePackageBase):

    def createPackage(self):
        self.defines["appname"] = "ghostwriter"
        self.defines["shortcuts"] = [{
            "name": "ghostwriter",
            "target": "bin/ghostwriter.exe"
        }]

        return super().createPackage()
